from django.conf import settings
from lighthive.client import Client
from lighthive.datastructures import Operation
from datetime import datetime
import json

_client = None


def get_client():
    global _client
    if not _client:
        _client = Client()

    return _client


def get_permlink(date_str):
    return "ramblings-%s" % date_str


def main_post_check(account):
    c = get_client()
    today_permlink = datetime.today().strftime('%Y-%m-%d')
    content = c.get_content(account, get_permlink(today_permlink))
    if content.get("id") == 0:
        print("No main post found. Creating one")
        post_daily_post(account, today_permlink)

    return today_permlink


def get_comment_options(author, permlink):

    comment_options = Operation('comment_options',  {
        'author': author,
        'permlink': permlink,
        'max_accepted_payout': '1000000.000 HBD',
        'percent_steem_dollars': '10000',
        'allow_votes': True,
        'allow_curation_rewards': True,
        'extensions': [
            [0, {
                "beneficiaries": [
                    {"account": "steem.dao", "weight": 2500},
                ]
            }]
        ]
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
        "json_metadata": json.dumps({"tags": [settings.COMMUNITY_TAG, "ramblings"]})
    })

    comment_options = get_comment_options(account, get_permlink(date_str))

    c = get_client()
    c.keys = [settings.POSTER_ACCOUNTER_KEY,]
    c.broadcast([post, comment_options])


def post_reply(account, date_str, title, body, permlink):
    template = """**%s**
    
%s

--
*See this post at [AnonRamblings](https://anonramblings.com/post/%s)*"""
    template = template % (title, body, permlink)

    post = Operation('comment', {
        "parent_author": account,
        "parent_permlink": get_permlink(date_str),
        "author": account,
        "permlink": permlink,
        "title": "Today's ramblings - %s" % date_str,
        "body": template,
        "json_metadata": json.dumps({"tags": [settings.COMMUNITY_TAG]})
    })

    comment_options = get_comment_options(account, permlink)

    c = get_client()
    c.keys = [settings.POSTER_ACCOUNTER_KEY, ]
    print(post, comment_options)
    print(c.broadcast([post, comment_options]))
