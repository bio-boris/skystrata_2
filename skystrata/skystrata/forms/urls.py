# from django.conf.urls import url,include
from .views import *
from django.urls import include, path, re_path
from django.contrib import admin




app_name = "skystrata.forms"



urlpatterns = [
    re_path(r'^admin/', admin.site.urls, name="admin"),
    # re_path(r'^templates/$', list_templates, name="list_templates"),
    # re_path(r'^templates/add/$', add_template, name="add_template"),
    # re_path(r'^templates/modify/(?P<pk>\d+)/$', modify_template, name="modify_template"),

    re_path(r'^templates/$', ListTemplates.as_view(), name="list_templates"),
    re_path(r'^templates/add/$', AddTemplate.as_view(), name="add_template"),
    re_path(r'^templates/modify/(?P<pk>\d+)/$', EditTemplate.as_view(), name="modify_template"),

    re_path(r'^instances/$', ListInstances.as_view(), name="list_instances"),
    re_path(r'^instances/add/$', LaunchInstance.as_view(), name="add_instance"),
    re_path(r'^instances/modify/(?P<pk>\d+)/$', EditInstance.as_view(), name="modify_instance"),

]
