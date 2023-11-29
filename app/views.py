from django.shortcuts import render

from django.http import HttpResponse

from .tasks import sleeptime

# Create your views here.

def home(request):

    sleeptime.delay(15) # .delay() Invokes celery instance to receive task

    return HttpResponse("I am about to wake up! Woke!! Testing....")