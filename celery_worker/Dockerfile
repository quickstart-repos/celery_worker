FROM python:3.9.4-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir worker_src
COPY worker_src/. worker_src

CMD celery -A worker_src worker --loglevel=INFO
