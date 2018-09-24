"""skystrata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import *
#
# from api import urls
from skystrata.forms import *
from skystrata.forms.views import *


urlpatterns = [
    path("templates/", TemplateView.as_view(template_name="pages/templates.html"), name="templates"),
    path("instances/", TemplateView.as_view(template_name="pages/instances.html"), name="instances"),
    path("register/", TemplateView.as_view(template_name="pages/register.html"), name="register"),
    path("metrics/", TemplateView.as_view(template_name="pages/metrics.html"), name="register"),
    path("home/", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('admin/', admin.site.urls),
    # re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^api/v1/', include('api.urls', namespace='api-skystrata')),

    re_path(r'^templates/$', ListTemplates.as_view(), name="list_templates"),
    re_path(r'^templates/add/$', AddTemplate.as_view(), name="add_template"),
    re_path(r'^templates/modify/(?P<pk>\d+)/$', EditTemplate.as_view(), name="modify_template"),

]
