# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

import time


@shared_task
def add(x, y):
    time.sleep(1)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task()
def enqueue(instance_pk, token):
    from subprocess import call
    bin = "/Users/bsadkhin/workspace/django/skystrata/skystrata/api/celery_home/start.py"
    command = ["python", bin, instance_pk, token]
    call(command)


def shutdown(instance_pk, token):
    pass
