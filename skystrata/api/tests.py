from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from skystrata.api.models import Template

from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


# Create your tests here.
class SkyStrataApiTests(APITestCase):

    def setUp(self):
        self.user_obj = User(username="test_api_user", email='test@test.com')
        self.user_obj.set_password("SomeRandomPassword")
        self.user_obj.save()
        Template.objects.create(label="Test", cpu=1, memory=1, io=1, disk=1, cost=1)
        Template.objects.create(label="Test2", cpu=2, memory=2, io=2, disk=2, cost=2)
        Template.objects.create(label="Test3", cpu=3, memory=3, io=3, disk=3, cost=3)

    def test_unauthenticated_templates_get_all(self):
        data = {}
        url = api_reverse("skystrata.api:templates-lc")
        # url = "http://127.0.0.1:8000/api/v1/templates/"
        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_templates_create(self):
        data = {}
        url = api_reverse("skystrata.api:templates-lc")
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #
    def test_unauthenticated_templates_post(self):
        data = {"label": "Test4", }
        url = api_reverse("skystrata.api:templates-lc")
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_templates_get_first(self):
        t1 = Template.objects.first()
        data = {}
        url = t1.get_api_uri()

        response = self.client.get(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_templates_update_first(self):
        t1 = Template.objects.first()
        data = {"label": "NewLabel"}
        url = t1.get_api_uri()

        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_templates_update_first(self):
        t1 = Template.objects.first()
        data = {"label": "NewLabel",
                "cpu": 1,
                "memory": 1,
                "io": 1,
                "disk": 1,
                "cost": 100}
        url = t1.get_api_uri()
        print(url)

        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_login(self.user_obj)
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(url, data, format='json')
        self.assertEquals(response.data['label'] , data['label'])

        # TEST OWNERSHIP EVENTUALLY
