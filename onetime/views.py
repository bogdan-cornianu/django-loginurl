from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponseGone
from django.contrib.auth import login
from django.conf import settings

from onetime import utils
from onetime.models import Key

def cleanup(request):
    utils.cleanup()

def login(request, key, redirect_invalid_to=None, redirect_expired_to=None):
    data = Key.objects.get(key=key)
    if data is None:
        if redirect_invalid_to is not None:
            return HttpResponseRedirect(redirect_invalid_to)
        else:
            return HttpResponseGone()

    expired = False
    if data.usage_left is not None and data.usage_left <= 0:
        expired = True
    if data.expires is not None and data.expires < datetime.now():
        expired = True

    if expired:
        if redirect_expired_to is not None:
            return HttpResponseRedirect(redirect_expired_to)
        else:
            return HttpResponseGone()

    if data.usage_left is not None:
        data.usage_left -= 1
        data.save()

    login(request, data.user)

    next = request.GET.get('next', None)
    if data.next is not None:
        next = data.next
    if next is None:
        next = settings.LOGIN_REDIRECT_URL

    return HttpResponseRedirect(next)

