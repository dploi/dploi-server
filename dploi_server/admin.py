#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Realm, Host, Deployment, Application,\
    Postgres, PostgresInstance, Gunicorn, GunicornInstance, Celery, CeleryInstance,\
    Redis, RedisInstance, Solr, SolrInstance




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


class PostgresInline(TabularInline):
    model = Postgres


class GunicornInline(TabularInline):
    model = Gunicorn


class CeleryInline(TabularInline):
    model = Celery


class RedisInline(TabularInline):
    model = Redis


class SolrInline(TabularInline):
    model = Solr


class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'ipv4', 'realm',)
    list_filter = ('realm',)
    inlines = (PostgresInline, GunicornInline, CeleryInline, RedisInline, SolrInline)


admin.site.register(Host, HostAdmin)


######################
# Application Admin  #
######################


class DeploymentInline(TabularInline):
    model = Deployment
    readonly_fields = ('identifier',)
    fields = ('name', 'is_live', 'branch', 'identifier',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'verbose_name', 'repository')
    inlines = (DeploymentInline,)


admin.site.register(Application, ApplicationAdmin)


#####################
# Deployment Admin  #
#####################


class PostgresInstanceInline(TabularInline):
    model = PostgresInstance


class GunicornInstanceInline(TabularInline):
    model = GunicornInstance


class CeleryInstanceInline(TabularInline):
    model = CeleryInstance


class RedisInstanceInline(TabularInline):
    model = RedisInstance


class SolrInstanceInline(TabularInline):
    model = SolrInstance


class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name', 'application', 'is_live',)
    list_filter = ('name',)
    readonly_fields = ('identifier',)
    inlines = (PostgresInstanceInline, GunicornInstanceInline, CeleryInstanceInline, RedisInstanceInline,
               SolrInstanceInline)


admin.site.register(Deployment, DeploymentAdmin)