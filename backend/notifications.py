import os
from celery import Celery

# Use environment variable for broker URL
broker_url = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')

celery_app = Celery('tasks', broker=broker_url)

@celery_app.task
def send_email_task(user_email):
    # email sending logic
    pass