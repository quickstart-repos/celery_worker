from celery import Celery
import os

required_variables = ['PROJECT_NAME', 'BROKER_USER', 'BROKER_PASS']

for var in required_variables:
    if var not in os.environ:
        print('You must define ' + var + ' environment variable')

worker_name = 'worker_src.' + os.environ['PROJECT_NAME']
broker_url = 'amqp://%s:%s@localhost' % (os.environ['BROKER_USER'], os.environ['BROKER_PASS'])

app = Celery('consumer', backend='redis://localhost', broker=broker_url)

def run_task(task_name, args):
    return app.send_task(worker_name + '.' + task_name, args)
