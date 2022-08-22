import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'google_sheets.settings')

app = Celery("google_sheets")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'refresh-base-every-minute': {  # Refresh google sheets -> DB, every minute
        'task': 'google_sheets_extraction_app.tasks.update_google_sheets.update_data',
        'schedule': crontab(),
    },
    'refresh-currency-rate': {  # Refresh currency rates, every day
        'task': 'google_sheets_extraction_app.tasks.exchange_rate.exchange_rate',
        'schedule': crontab(hour=1),
        'args': ('USD', 'UAH')
    },
}

