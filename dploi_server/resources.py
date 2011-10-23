#-*- coding: utf-8 -*-
from djangorestframework.resources import ModelResource
from .models import Realm, Application, Deployment


#class RealmResource(ModelResource):
#    model = Application
#    fields = ('name', 'verbose_name', 'description', 'repository')
#    ordering = ('name',)

class ApplicationResource(ModelResource):
    model = Application
    fields = (
        'name', 'verbose_name', 'description', 'repository',
        ('deployments',
            ('identifier', 'is_live', 'name', 'branch',
                ('domains', ('name',)),
                ('redirect_domains', ('name',)),
                ('postgres_instances', ('alias', 'name', 'user', 'password', 'service',)),
            )
        ),
    )
    ordering = ('name',)
    depth = 1