#-*- coding: utf-8 -*-
from djangorestframework.resources import ModelResource, FormResource
from dploi_server.models import PostgresInstance, LoadBalancer
from .models import Realm, Application, Deployment


#class RealmResource(ModelResource):
#    model = Application
#    fields = ('name', 'verbose_name', 'description', 'repository')
#    ordering = ('name',)

class ApplicationResource(ModelResource):
    model = Application
    fields = (
        'name', 'verbose_name', 'description', 'repository',
#        ('deployments',
#            ('identifier', 'is_live', 'name', 'branch',
#                ('domains', ('name',)),
#                ('redirect_domains', ('name',)),
#                ('postgres_instances', ('alias', 'name', 'user', 'password', 'service',)),
#            )
#        ),
    )
    ordering = ('name',)
    depth = 1


class PostgresDatabaseConfigResource(FormResource):
    model = PostgresInstance
    fields = ('alias', 'host', 'port', 'user', 'password')

    def host(self, instance):
        return instance.service.host.private_ipv4

    def port(self, instance):
        return instance.service.port

class LoadBalancerConfigResource(FormResource):
    model = LoadBalancer
    fields = ('ipv4',)

    def ipv4(self, instance):
        return instance.host.public_ipv4


class DeploymentConfigResource(FormResource):
    model = Deployment
    fields = (
        'identifier', 'name', 'branch', 'is_live',
        ('postgres_instances', PostgresDatabaseConfigResource),
        ('load_balancer', LoadBalancerConfigResource)
    )


class ApplicationConfigResource(ModelResource):
    model = Application
    fields = (
        'name', 'verbose_name', 'description', 'repository',
        ('deployments', DeploymentConfigResource)
    )
    ordering = ('name',)
    depth = 1