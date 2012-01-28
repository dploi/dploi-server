#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from dploi_server.models import Deployment
from dploi_server_ui.views import OverviewView, RealmList, ApplicationList, ApplicationDetail, ApplicationUpdate, DeploymentUpdate, DeploymentDetail

urlpatterns = patterns('',
    url(r'^$', OverviewView.as_view(), name="dploi_overview"),
    url(r'^realms/$', RealmList.as_view(), name="dploi_realm_list"),
    url(r'^applications/$', ApplicationList.as_view(), name="dploi_application_list"),
    url(r'^applications/(?P<pk>\d+)/$', ApplicationDetail.as_view(), name="dploi_application_detail"),
    url(r'^applications/(?P<pk>\d+)/edit/$', ApplicationUpdate.as_view(), name="dploi_application_update"),
    url(r'^applications/deployment/(?P<pk>\d+)/$', DeploymentDetail.as_view(), name="dploi_deployment_detail"),
    url(r'^applications/deployment/(?P<pk>\d+)/edit/$', DeploymentUpdate.as_view(), name="dploi_deployment_update"),
)