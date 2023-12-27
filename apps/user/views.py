from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .tasks import test_user


def index(request: HttpRequest):
    test_user.delay()
    return HttpResponse(f"Hello user - {request.user.is_authenticated}")
