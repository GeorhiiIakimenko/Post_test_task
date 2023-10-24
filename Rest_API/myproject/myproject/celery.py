import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'collect-post-analytics-every-day': {
        'task': 'evoapp.tasks.collect_post_analytics',
        'schedule': crontab(minute=59, hour=23),  # Every day at 23:59
    },
}
