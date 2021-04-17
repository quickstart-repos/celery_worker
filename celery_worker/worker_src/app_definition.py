import os
from celery import Celery

def build_celery_app(project_name,
    broker_url, state_storage_url, broker_user, broker_pass,
    broker_port=5672, state_storage_port=6379):

    broker_url = 'amqp://%s:%s@%s:%d' % (broker_user, broker_pass, broker_url, broker_port)
    redis_url = 'redis://%s:%s' % (state_storage_url, state_storage_port)

    app = Celery(project_name, broker=broker_url, backend=redis_url,
    include=['worker_src.tasks'])

    return app
