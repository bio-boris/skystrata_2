from collections import namedtuple


from .tasks import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


status = namedtuple("status", "command result")
User = get_user_model()


def start_instance(instance,request):


    token = Token.objects.get(user=request.user)
    if token is None:
        raise Exception("Token not found for user")

    pk = str(instance.pk)
    enqueue.delay(pk,str(token))



def stop_instance(request, instance_id):
    token = 1  # request.token
    print("Stopping instance")
    return 1


def getStatus(request, instance_id):
    print("Stopping instance")
    return status(command="Stop", result="OK")


def __startUp(settings=None):
    print("Starting up instance")
    return status(command="Start", result="OK")


def __shutDown(settings=None):
    print("Stopping instance")
    return status(command="Stop", result="OK")
