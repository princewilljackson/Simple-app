from celery import shared_task
from django.core.mail import send_mail
from config import settings

from time import sleep

@shared_task
def sleeptime(total_time):
    sleep(total_time)
    return None

@shared_task(bind=True)
def send_notification_mail(self, target_mail, message):
    mail_subject = "Welcome on Board!"
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
        )
    return "Done"