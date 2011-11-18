#-*- coding: utf-8 -*-
from djangorestframework.resources import ModelResource, FormResource
from dploi_server.models import PostgresInstance, LoadBalancer, DomainAlias, GunicornInstance
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
        return instance.service.host.hostname

    def port(self, instance):
        return instance.service.port

class LoadBalancerConfigResource(FormResource):
    model = LoadBalancer
    fields = ('ipv4',)

    def ipv4(self, instance):
        return instance.host.public_ipv4

class DomainAliasConfigResource(FormResource):
    model = DomainAlias # Doesnt seem to be used?
    fields = ('name',)

class GunicornInstanceConfigResource(FormResource):
    model = GunicornInstance # Doesnt seem to be used?
    fields = ('workers', 'max_requests', 'ipv4', 'hostname')

    def hostname(self, instance):
        return instance.service.host.hostname

    def ipv4(self, instance):
        # TODO: Use hostname instead of ipv4/ipv6?
        return instance.service.host.public_ipv4


class DeploymentConfigResource(FormResource):
    model = Deployment

    def path(self, instance):
        return "/home/%s/app/" % instance.identifier

    def backup_dir(self, instance):
            return "/home/%s/tmp/" % instance.identifier

    fields = (
        'identifier', 'name', 'branch', 'is_live', 'path', 'backup_dir', 'domains',
        ('postgres_instances', PostgresDatabaseConfigResource),
        ('load_balancer', LoadBalancerConfigResource),
        ('domain_aliases', DomainAliasConfigResource),
        ('gunicorn_instances', GunicornInstanceConfigResource),
    )


class ApplicationConfigResource(ModelResource):
    model = Application
    fields = (
        'name', 'verbose_name', 'description', 'repository',
        ('deployments', DeploymentConfigResource)
    )
    ordering = ('name',)
    depth = 1