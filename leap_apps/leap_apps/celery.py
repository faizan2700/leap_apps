# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leap_apps.settings')

app = Celery('leap_apps')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY') 

app.conf.broker_url = 'memory://'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()