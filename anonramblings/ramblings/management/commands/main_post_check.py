import logging
import time

from django.core.management.base import BaseCommand

from django.conf import settings

from ramblings.utils import main_post_check, post_reply
from ramblings.models import Post

from datetime import datetime

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            main_post_permlink = main_post_check(settings.POSTER_ACCOUNT)

            for post in Post.objects.filter(sent_to_blockchain=False).order_by("-pk"):
                try:
                    if post.parent:
                        reply_to_permlink = post.parent.permlink
                    else:
                        reply_to_permlink = None
                    post_reply(settings.POSTER_ACCOUNT, main_post_permlink, post.title, post.body, post.permlink, reply_to_permlink=reply_to_permlink)
                    post.sent_to_blockchain = True
                    post.save()
                    print("Saved", post.permlink)
                except Exception as e:
                    logger.error(e)

            time.sleep(10)
