from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .tasks import test


def index(request: HttpRequest):
    test.delay()
    return HttpResponse("Hello")
