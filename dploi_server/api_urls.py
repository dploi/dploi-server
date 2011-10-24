#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from dploi_server.resources import ApplicationConfigResource
from .resources import ApplicationResource

urlpatterns = patterns('',
    url(r'^applications/$',          ListOrCreateModelView.as_view(resource=ApplicationResource), name='application-resource-root'),
    url(r'^applications/(?P<name>[a-z0-9_]+)/$', InstanceModelView.as_view(resource=ApplicationResource)),
    url(r'^applications/(?P<name>[a-z0-9_]+)/config/$', InstanceModelView.as_view(resource=ApplicationConfigResource)),
)