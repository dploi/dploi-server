#-*- coding: utf-8 -*-
from django.contrib import admin
from dploi_server.models import (Realm, Host,
              Postgres, Gunicorn, RabbitMq, Celery, Redis, Solr,
              Application, Deployment, DomainName, DomainAlias, DomainRedirect,
              PostgresInstance, GunicornInstance, RabbitMqInstance, CeleryInstance, RedisInstance, SolrInstance, LoadBalancer)




###############
# Base Admins #
###############

class TabularInline(admin.TabularInline):
    extra = 0


###############
# Realm Admin #
###############


class HostInline(TabularInline):
    model = Host
    can_delete = False


class RealmAdmin(admin.ModelAdmin):
    inlines = (HostInline,)


admin.site.register(Realm, RealmAdmin)


##############
# Host Admin #
##############


class LoadBalancerInline(TabularInline):
    model = LoadBalancer


class PostgresInline(TabularInline):
    model = Postgres


class GunicornInline(TabularInline):
    model = Gunicorn


class RabbitMqInline(TabularInline):
    model = RabbitMq


class CeleryInline(TabularInline):
    model = Celery


class RedisInline(TabularInline):
    model = Redis


class SolrInline(TabularInline):
    model = Solr


class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'public_ipv4', 'private_ipv4', 'realm',)
    list_filter = ('realm',)
    inlines = (LoadBalancerInline, PostgresInline, GunicornInline, RabbitMqInline, CeleryInline, RedisInline, SolrInline)


admin.site.register(Host, HostAdmin)


######################
# Application Admin  #
######################


class DeploymentInline(TabularInline):
    model = Deployment
    fields = ('name', 'is_live', 'branch', 'identifier',)
    readonly_fields = ('identifier',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'verbose_name', 'repository')
    inlines = (DeploymentInline,)


admin.site.register(Application, ApplicationAdmin)


#####################
# Deployment Admin  #
#####################


class DomainAliasInline(TabularInline):
    model = DomainAlias


class DomainRedirectInline(TabularInline):
    model = DomainRedirect


class PostgresInstanceInline(TabularInline):
    model = PostgresInstance
    readonly_fields = ('name', 'user', 'password',)


class GunicornInstanceInline(TabularInline):
    model = GunicornInstance


class RabbitMqInstanceInline(TabularInline):
    model = RabbitMqInstance
    readonly_fields = ('virtual_host', 'user', 'password',)


class CeleryInstanceInline(TabularInline):
    model = CeleryInstance


class RedisInstanceInline(TabularInline):
    model = RedisInstance
    readonly_fields = ('access_token',)


class SolrInstanceInline(TabularInline):
    model = SolrInstance
    readonly_fields = ('name', 'password',)


class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name', 'application', 'is_live',)
    list_filter = ('name',)
    readonly_fields = ('identifier',)
    inlines = (DomainAliasInline, DomainRedirectInline,
               PostgresInstanceInline, GunicornInstanceInline, RabbitMqInstanceInline, CeleryInstanceInline,
               RedisInstanceInline, SolrInstanceInline)


admin.site.register(Deployment, DeploymentAdmin)

##########
# Domain #
##########


admin.site.register(DomainName)