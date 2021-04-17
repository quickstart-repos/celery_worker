import os
from celery import Celery
from worker_src.app_definition import *

required_environment_variables = ['PROJECT_NAME', 'BROKER_USER', 'BROKER_PASS']

for env in required_environment_variables:
    if env not in os.environ:
        print('You must provide a value for the ' + env + ' environment variable')
        exit(1)

project_name = os.environ['PROJECT_NAME']
broker_user = os.environ['BROKER_USER']
broker_pass = os.environ['BROKER_PASS']

app = build_celery_app(project_name, 'message_broker', 'state_storage', broker_user, broker_pass)

if __name__ == '__main__':
    app.start()
