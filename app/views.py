from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import SubscribeForm
from .tasks import sleeptime, send_notification_mail

from django.http import HttpResponse

# Create your views here.

# def home(request):

#     sleeptime.delay(15) # .delay() Invokes celery instance to receive task

#     return HttpResponse("I am about to wake up! Woke!! Testing....")

class IndexView(FormView):
    template_name = 'index.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        mail = form.cleaned_data["mail"]
        message = form.cleaned_data["message"]
        send_notification_mail.delay(mail, message)
        return HttpResponse('We have sent you a confirmation mail!')