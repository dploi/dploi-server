#-*- coding: utf-8 -*-
from djangorestframework.resources import ModelResource
from .models import Realm, Application, Deployment


#class RealmResource(ModelResource):
#    model = Application
#    fields = ('name', 'verbose_name', 'description', 'repository')
#    ordering = ('name',)

class ApplicationResource(ModelResource):
    model = Application
    fields = ('name', 'verbose_name', 'description', 'repository')
    ordering = ('name',)