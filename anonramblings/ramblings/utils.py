from lighthive.client import Client
import json
import re
import time
from datetime import datetime
from functools import partial

import bleach
import markdown
from django.conf import settings
from django.utils.safestring import mark_safe
from lighthive.client import Client
from lighthive.datastructures import Operation

APP_NAME = "anonramblings/0.0.1"


_client = None


def get_client():
    global _client
    if not _client:
        _client = Client(nodes=["https://api.hive.blog"])

    return _client


def get_permlink(date_str):
    return "ramblings-%s" % date_str


def main_post_check(account):
    c = get_client()
    today_permlink = datetime.today().strftime('%Y-%m-%d')
    try:
        content = c.get_content(account, get_permlink(today_permlink))
    except Exception as e:
        # after hf24, if the permlink is invalid, api returns an error
        content = {"id": 0}

    if content.get("id") == 0:
        print("No main post found. Creating one")
        post_daily_post(account, today_permlink)
        time.sleep(300)
    return today_permlink


def get_comment_options(author, permlink):
    comment_options = Operation('comment_options',  {
        'author': author,
        'permlink': permlink,
        'max_accepted_payout': '1000000.000 HBD',
        'percent_hive_dollars': '10000',
        'allow_votes': True,
        'allow_curation_rewards': True,
        'extensions': []
    })

    return comment_options


def post_daily_post(account, date_str):

    post = Operation('comment', {
        "parent_author": "",
        "parent_permlink": settings.COMMUNITY_TAG,
        "author": account,
        "permlink": get_permlink(date_str),
        "title": "Today's ramblings - %s" % date_str,
        "body": settings.MAIN_POST_CONTENT,
        "json_metadata": json.dumps({"tags": [settings.COMMUNITY_TAG, "ramblings"], "app": APP_NAME})
    })

    comment_options = get_comment_options(account, get_permlink(date_str))

    c = get_client()
    c.keys = [settings.POSTER_ACCOUNTER_KEY,]
    c.broadcast([post, comment_options])


def post_reply(account, date_str, title, body, permlink, reply_to_permlink=None):
    template = """**%s**
    
%s

--
*See this post at [AnonRamblings](https://anonramblings.com/post/%s)*"""
    template = template % (title, body, permlink)

    parent_permlink = get_permlink(date_str)
    if reply_to_permlink:
        parent_permlink = reply_to_permlink
    post = Operation('comment', {
        "parent_author": account,
        "parent_permlink": parent_permlink,
        "author": account,
        "permlink": permlink,
        "title": "Today's ramblings - %s" % date_str,
        "body": template,
        "json_metadata": json.dumps({"tags": [settings.COMMUNITY_TAG], "app": APP_NAME})
    })

    comment_options = get_comment_options(account, permlink)

    c = get_client()
    c.keys = [settings.POSTER_ACCOUNTER_KEY, ]
    print(c.broadcast([post, comment_options]))


def markdownify(text):
    # Bleach settings
    whitelist_tags = getattr(settings, 'MARKDOWNIFY_WHITELIST_TAGS', bleach.sanitizer.ALLOWED_TAGS)
    whitelist_attrs = getattr(settings, 'MARKDOWNIFY_WHITELIST_ATTRS', bleach.sanitizer.ALLOWED_ATTRIBUTES)
    whitelist_styles = getattr(settings, 'MARKDOWNIFY_WHITELIST_STYLES', bleach.sanitizer.ALLOWED_STYLES)
    whitelist_protocols = getattr(settings, 'MARKDOWNIFY_WHITELIST_PROTOCOLS', bleach.sanitizer.ALLOWED_PROTOCOLS)

    # Markdown settings
    strip = getattr(settings, 'MARKDOWNIFY_STRIP', True)
    extensions = getattr(settings, 'MARKDOWNIFY_MARKDOWN_EXTENSIONS', [])

    # Bleach Linkify
    linkify = None
    linkify_text = getattr(settings, 'MARKDOWNIFY_LINKIFY_TEXT', True)

    if linkify_text:
        linkify_parse_email = getattr(settings, 'MARKDOWNIFY_LINKIFY_PARSE_EMAIL', False)
        linkify_callbacks = getattr(settings, 'MARKDOWNIFY_LINKIFY_CALLBACKS', None)
        linkify_skip_tags = getattr(settings, 'MARKDOWNIFY_LINKIFY_SKIP_TAGS', None)
        linkifyfilter = bleach.linkifier.LinkifyFilter

        linkify = [partial(linkifyfilter,
                callbacks=linkify_callbacks,
                skip_tags=linkify_skip_tags,
                parse_email=linkify_parse_email
                )]

    # Convert markdown to html
    html = markdown.markdown(text, extensions=extensions)

    # Sanitize html if wanted
    if getattr(settings, 'MARKDOWNIFY_BLEACH', True):

        cleaner = bleach.Cleaner(tags=whitelist_tags,
                                 attributes=whitelist_attrs,
                                 styles=whitelist_styles,
                                 protocols=whitelist_protocols,
                                 strip=strip,
                                 filters=linkify,
                                 )

        html = cleaner.clean(html)

        # ugly hack to use hive's image server
        html = re.sub(
            r'src="(.*?)"', r'src="https://images.hive.blog/0x0/\1"', html)

    return mark_safe(html)
