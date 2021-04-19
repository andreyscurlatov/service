import os
from celery import Celery
from celery.schedules import crontab



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('service', broker='redis://127.0.0.1:6379/0')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'recruitment.tasks.sendPeriodicMail',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}


