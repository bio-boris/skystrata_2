# from django.conf.urls import url,include
from django.contrib import admin
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views

from .views import *

app_name = "skystrata.api"

schema_view = get_swagger_view(title='SkyStrata API')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    # images
    re_path(r'^images/(?P<pk>\d+)/$', ImageRudView.as_view(), name='image-rud'),
    re_path(r'^images/$', ImageLCView.as_view(), name='image-lc'),

    # cloudproviders
    re_path(r'^cloudproviders/(?P<pk>\d+)/$', CloudProviderRudView.as_view(),
            name='cloud-provider-rud'),
    re_path(r'^cloudproviders/$', CloudProviderLCView.as_view(), name='cloud-provider-lc'),

    # provideroptions
    re_path(r'^provideroptions/(?P<pk>\d+)/$', ProviderOptionRudView.as_view(),
            name='provideroptions-rud'),
    re_path(r'^provideroptions/$', ProviderOptionLCView.as_view(), name='provideroptions-lc'),

    # templates
    re_path(r'^templates/(?P<pk>\d+)/$', TemplateRUDView.as_view(),
            name='templates-rud'),
    re_path(r'^templates/$', TemplateLCView.as_view(), name='templates-lc'),

    # #Templates test
    # re_path(r'^templates2/(?P<pk>\d+)/$', TemplateList.as_view(),name='templates-lc'),
    # re_path(r'^templates2//$', TemplateList.as_view(),name='templates-rud-detail'),

    # Instances
    re_path(r'^instances/(?P<pk>\d+)/$', InstanceRUDView.as_view(), name='instances-rud'),
    re_path(r'^instances/$', InstanceLCView.as_view(), name='instances-lc'),


    # swagger
    re_path(r'^swagger_schema/$', schema_view),

    re_path(r'^^api-token-auth/$', CustomAuthToken.as_view()),

    re_path(r'^view_celery/$', viewCelery),


]

# Add suffix patterns such as .json
urlpatterns = format_suffix_patterns(urlpatterns)
