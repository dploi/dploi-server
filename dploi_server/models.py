#-*- coding: utf-8 -*-
import random
from django.db import models
from dploi_server.utils.password import generate_password
from dploi_server.validation import variable_name_validator, variable_name_and_dash_validator


class Realm(models.Model):
    """
    A realm is the root object of the whole system.

    The main building blocks of a Realm are:

    * Host - A physical (or virtual) machine with an IP address
    * Application - The Software/Application
    * Deployment - The Deployment of an Application. (e.g live or dev deployment of ApplicationX)
    * Service - A server that provides a service (to multiple different clients). E.g Postgres or Solr
    * Instance - A usage of a Service by a Deployment (e.g the database for project X live)
    * Process - A Deployment specific Process (Daemon) running on a Host (e.g gunicorn, celery-worker)
    """
    name = models.CharField(max_length=255, validators=[variable_name_validator], unique=True)
    verbose_name = models.CharField(max_length=255)
    base_domain = models.CharField(max_length=255, help_text='used for inital deployment domains. e.g myproject-live.basedomain.com')
    puppet_repository = models.CharField(max_length=255, blank=True, default='')
    puppet_repository_private_key = models.TextField(blank=True, default='')
    puppet_repository_public_key = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.verbose_name or self.name


class Host(models.Model):
    """
    A physical (or virtual) machine with an IP address
    """
    realm = models.ForeignKey(Realm, related_name='hosts')
    name = models.CharField(max_length=255, validators=[variable_name_and_dash_validator])
    public_ipv4 = models.CharField(max_length=15)
    private_ipv4 = models.CharField(max_length=15)

    def hostname(self):
        return "%s.%s" % (self.name, self.realm.base_domain)

    class Meta:
        unique_together = ('realm', 'name')

    def __unicode__(self):
        return u"%s" % (self.name,)


############
# Services #
############

class BaseService(models.Model):
    host = models.ForeignKey(Host, related_name='%(class)ss')
    is_enabled = models.BooleanField()  # mainly here so that inlines display correctly in admin ;-P

    class Meta:
        abstract=True

    def __unicode__(self):
        return u"%s (%s)" % (self.__class__.__name__, self.host)


class LoadBalancer(BaseService):
    pass


class Postgres(BaseService):
    port = models.IntegerField(default=5432)


class Gunicorn(BaseService):
    pass


class Celery(BaseService):
    """
    A container for processes that handle out of request jobs. (celeryd, celerybeat)
    """
    pass


class Redis(BaseService):
    """
    Redis runs a seperate process for each database... so there isn't anything to configure here
    """
    pass


class RabbitMq(BaseService):
    """
    RabbitMQ Service on one specific server. This is a "Node" in RabbitMQ speak
    """
    port = models.IntegerField(default=5432)


class Solr(BaseService):
    port = models.IntegerField(default=8983)


##############################
# Application and Deployment #
##############################


class Application(models.Model):
    """
    The Software/Application
    """
    name = models.CharField(max_length=255, unique=True)
    verbose_name = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, default='')
    repository = models.CharField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return u"%s" % (self.verbose_name or self.name,)


class Deployment(models.Model):
    """
    A deployment of an application.
    """
    application = models.ForeignKey(Application, related_name='deployments')
    is_live = models.BooleanField(default=False)
    identifier = models.CharField(max_length=255, unique=True, validators=[variable_name_and_dash_validator],
                                  help_text='system wide unique identifier of this deplpyment')
    name = models.CharField(max_length=255, validators=[variable_name_validator])
    description = models.TextField(blank=True, default='')
    private_key = models.TextField(blank=True, default='', help_text='private deployment ssh key for source code access')
    public_key = models.TextField(blank=True, default='', help_text='public deployment ssh key for source code access')
    branch = models.CharField(max_length=255, default='develop', help_text="branch or tag for this deployment")
    load_balancer = models.ForeignKey(LoadBalancer, related_name='deployments', null=True, blank=True)

    def domains(self):
        # TODO: Find a better way to lookup base domain(s)
        return [{'name': "%s.%s" % (self.identifier, gunicorn.service.host.realm.base_domain)} for gunicorn in self.gunicorn_instances.all()]

    class Meta:
        unique_together = (('application', 'name',),)

    # Defaults
    
    def get_default_identifier(self):
        return u"%s-%s" % (self.application.name, self.name)


class DomainName(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return u"%s" % self.name


class DomainAlias(DomainName):
    deployment = models.ForeignKey(Deployment, related_name='domain_aliases')


class DomainRedirect(DomainName):
    deployment = models.ForeignKey(Deployment, related_name='domain_redirects')


class PostgresInstance(models.Model):
    service = models.ForeignKey(Postgres, related_name='instances')
    deployment = models.ForeignKey(Deployment, related_name='postgres_instances')

    alias = models.CharField(max_length=255, default='default', validators=[variable_name_validator],
                             help_text="Used as the django database alias.")
    name = models.CharField(max_length=255, help_text="postgres database name", validators=[variable_name_and_dash_validator])
    user = models.CharField(max_length=255, validators=[variable_name_and_dash_validator])
    password = models.CharField(max_length=255)

    class Meta:
        unique_together = ('name', 'service',)

    def __unicode__(self):
        return u"%s-%s" % (self.service, self.deployment,)

    # Default values
    def get_default_name(self):
        return self.deployment.identifier

    def get_default_user(self):
        return self.deployment.identifier

    def get_default_password(self):
        return generate_password()


class GunicornInstance(models.Model):
    service = models.ForeignKey(Gunicorn, related_name='instances')
    deployment = models.ForeignKey(Deployment, related_name='gunicorn_instances')

    workers = models.PositiveSmallIntegerField(default=3)
    max_requests = models.PositiveSmallIntegerField(default=2000)


class RabbitMqInstance(models.Model):
    service = models.ForeignKey(RabbitMq, related_name='instances')
    deployment = models.ForeignKey(Deployment, related_name='rabbitmq_instances')

    virtual_host = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        unique_together = ('virtual_host', 'service')

    # Default values
    def get_default_virtual_host(self):
        return self.deployment.identifier

    def get_default_user(self):
        return self.deployment.identifier

    def get_default_password(self):
        return generate_password()


class CeleryInstance(models.Model):
    service = models.ForeignKey(Celery, related_name='instances')
    deployment = models.ForeignKey(Deployment, related_name='celery_instances')

    workers = models.PositiveSmallIntegerField(default=3)
    fire_events = models.BooleanField(default=False,
        help_text="When active there MUST be another process consuming the events (celerycam). " + \
                  "Or else the queue will drown in messages.")
    beat = models.BooleanField(default=True,
        help_text="only one celery instance per deployment should have this option active.")


class RedisInstance(models.Model):
    service = models.ForeignKey(Redis, related_name='instances')
    deployment = models.ForeignKey(Deployment, related_name='redis_instances')

    port = models.IntegerField()
    access_token = models.CharField(max_length=255)

    class Meta:
        unique_together = ('service', 'port',)

    def get_default_port(self):
        return random.randrange(50000,52000)

    def get_default_access_token(self):
        return generate_password(length=30)


class SolrInstance(models.Model):
    service = models.ForeignKey(Solr, related_name='instances')
    deployment = models.ForeignKey(Deployment, related_name='solr_instances')

    name = models.CharField(max_length=255, help_text="solr core name (multicore)")
    password = models.CharField(max_length=255)

    class Meta:
        unique_together = ('name', 'service')
    
    def get_default_name(self):
        return self.deployment.identifier

    def get_default_password(self):
        return generate_password()



###########
# Signals #
###########

from django.db.models.signals import pre_save

def set_defaults(sender, **kwargs):
    """
    looks for methods called set_default_<fieldname> on instance and assignes its return value
    to <fieldname> if instance.<fieldname> is not set yet (either None or '').
    """
    instance = kwargs.get('instance')
    for thing in dir(instance):
        empty, duck, field_name = thing.partition('get_default_')
        if not empty and duck and hasattr(instance, field_name):
            value = getattr(instance, field_name)
            if value in (None, ''):
                default_value = getattr(instance, thing)
                if callable(default_value):
                    default_value = default_value()
                setattr(instance, field_name, default_value)
pre_save.connect(set_defaults)