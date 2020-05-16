from django.db import models
from django.utils.html import strip_tags

from markdownx.models import MarkdownxField
from .utils import markdownify

import uuid


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    permlink = models.CharField(max_length=36, unique=True, db_index=True)
    body = MarkdownxField(max_length=5000)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    is_approved = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    sent_to_blockchain = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def formatted_body(self):
        body = strip_tags(self.body)
        return markdownify(body)

    @property
    def formatted_summary(self):
        body = strip_tags(self.body)
        return markdownify(body)[0:300] + ('<small><a href="/post/%s"> → Read more</a> </small>' % self.permlink)

    def save(self, *args, **kwwargs):

        if not self.permlink:
            self.permlink = str(uuid.uuid4())
        super().save(*args, **kwwargs)



