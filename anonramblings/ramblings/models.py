from django.db import models
from django.utils.html import strip_tags

from markdownx.models import MarkdownxField
from .utils import markdownify
from .random_name_generator import get_random_name
from mptt.models import MPTTModel, TreeForeignKey
import uuid


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(MPTTModel):
    title = models.CharField(max_length=255)
    permlink = models.CharField(max_length=36, unique=True, db_index=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.DO_NOTHING)
    body = MarkdownxField(max_length=5000)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    is_approved = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    sent_to_blockchain = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_post = None

    def __str__(self):
        return self.title

    @property
    def formatted_body(self):
        body = strip_tags(self.body)
        return markdownify(body)

    @property
    def parent_post(self):
        if not self._parent_post:
            self._parent_post = self.parent
        return self._parent_post

    @property
    def formatted_summary(self):
        body = strip_tags(self.body)
        if len(body) > 300:
            return markdownify(body)[0:300] + ('<small><a href="/post/%s"> → Read more</a> </small>' % self.permlink)
        return markdownify(body)

    def update_ancestors(self):
        for ancestor in self.get_ancestors():
            ancestor.comment_count = ancestor.get_descendants().count()
            ancestor.save()

    def save(self, *args, **kwwargs):

        if not self.permlink:
            self.permlink = str(uuid.uuid4())
        if not self.nickname:
            self.nickname = get_random_name()

        self.update_ancestors()

        super().save(*args, **kwwargs)

    class MPTTMeta:
        order_insertion_by=['id']

    class Meta:
        ordering=['tree_id','lft']


