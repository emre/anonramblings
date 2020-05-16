from django.conf import settings


def settings_processor(request):
    return {
        'poster_account': settings.POSTER_ACCOUNT,
        'debig': settings.DEBUG,
    }