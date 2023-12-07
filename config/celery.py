from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/Paris')

# CELERY BEAT SETTINGS

app.conf.beat_schedule = {
    'send-ad-mail-every-day': {
        'task': 'app.tasks.send_ad_mails',
        'schedule': crontab(hour=15, minute=56),
        'args' : ("I am a Nigerian Prince.",)
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')