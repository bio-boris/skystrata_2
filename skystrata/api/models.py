from django.db import models
from rest_framework.reverse import reverse as api_reverse

from django.contrib.auth import get_user_model
from enum import Enum

# Create your models here.

# class ActionChoices(Enum):  # A subclass of Enum
#     START = "START"
#     STOP = "STOP"
#     PAUSE = "PAUSE"

#
# class Command(models.Model):
#
#
#
#     label = models.CharField(max_length=255, blank=False)
#     action = models.CharField(
#         max_length=255, blank=False ,
#         choices=[(tag, tag.value) for tag in ActionChoices]
#     )
#



# class Customer(models.Model):
#
#     name = models.CharField(max_length=255, blank=False)
#     address = models.TextField(blank=False)
#     email = models.CharField(max_length=255, blank=False)
#     phone = models.CharField(max_length=255, blank=False)
#     timezone = models.CharField(max_length=255, blank=False)
#     modified_date = models.DateTimeField(auto_now=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.name)


# Amazon, Azure
class CloudProvider(models.Model):
    label = models.CharField(max_length=255, blank=False)
    api = models.TextField(blank=False)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_api_uri(self, request=None):
        return api_reverse("skystrata.api:cloud-provider-rud", kwargs={'pk': self.pk},
                           request=request)

    def __str__(self):
        return str(self.label)


# FK is CloudProvider
class ProviderOption(models.Model):
    label = models.CharField(max_length=255, blank=False)
    provider = models.ForeignKey(CloudProvider, on_delete=models.CASCADE)
    cost = models.FloatField(blank=False)
    cpu_score = models.FloatField(blank=False)
    network_score = models.FloatField(blank=False)
    memory_score = models.FloatField(blank=False)
    throughput_score = models.FloatField(blank=False)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_api_uri(self, request=None):
        return api_reverse("skystrata.api:provideroptions-rud", kwargs={'pk': self.pk},
                           request=request)

    def __str__(self):
        return str(self.label)


class Image(models.Model):
    label = models.CharField(max_length=255, blank=False)
    provider = models.ForeignKey(CloudProvider, on_delete=models.CASCADE)
    repository_url = models.URLField(blank=False)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_api_uri(self, request=None):
        return api_reverse("skystrata.api:image-rud", kwargs={'pk': self.pk}, request=request)

    def __str__(self):
        return str(self.label)


class Template(models.Model):
    label = models.CharField(max_length=255, blank=False)
    cpu = models.FloatField(blank=False)
    memory = models.FloatField(blank=False)
    io = models.FloatField(blank=False)
    disk = models.FloatField(blank=False)
    cost = models.FloatField(blank=True,default=0)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_api_uri(self, request=None):
        return api_reverse("skystrata.api:templates-rud", kwargs={'pk': self.pk}, request=request)

    def __str__(self):
        return str(self.label)


class InstanceState(models.Model):
    label = models.CharField(max_length=255, blank=False, default=None)

    def __str__(self):
        return str(self.label)



class Instance(models.Model):
    label = models.CharField(max_length=255, blank=False)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    state = models.ForeignKey(InstanceState, on_delete=models.CASCADE, default=2)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.label)

    def get_api_uri(self, request=None):
        return api_reverse("skystrata.api:instances-rud", kwargs={'pk': self.pk}, request=request)

    def get_state(self, request=None):
        return self.state.label


class Bill(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, default=None)
    cost = models.FloatField(blank=False)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cost)


    def get_api_uri(self, request=None):
        return api_reverse("skystrata.api:bill-rud", kwargs={'pk': self.pk}, request=request)
