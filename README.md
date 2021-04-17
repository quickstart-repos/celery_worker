# First steps
This repository aims to provide an exemple for running a celery worker and define tasks for it.

The docker-compose.yml file will start a rabbitmq message broker, redis for task state storage 
and a docker celery worker.

In order to set the message broker management user and password, you must set the 
**BROKER_USER** and **BROKER_PASS** variables. You also must define the **PROJECT_NAME** 
environment variable, which will be used to identify the celery worker.


On linux

```
export BROKER_USER=<something>
export BROKER_PASS=<something>
export PROJECT_NAME=<something>

docker build
docker-compose up
```

On Windows Powershell

```
$Env:PROJECT_NAME = <something>
$Env:BROKER_USER = <something>
$Env:BROKER_PASS = <something>

docker build
docker-compose up
```
