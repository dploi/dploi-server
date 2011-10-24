# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Realm'
        db.create_table('dploi_server_realm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('base_domain', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('puppet_repository', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('puppet_repository_private_key', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('puppet_repository_public_key', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('dploi_server', ['Realm'])

        # Adding model 'Host'
        db.create_table('dploi_server_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('realm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hosts', to=orm['dploi_server.Realm'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('public_ipv4', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('private_ipv4', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('dploi_server', ['Host'])

        # Adding unique constraint on 'Host', fields ['realm', 'name']
        db.create_unique('dploi_server_host', ['realm_id', 'name'])

        # Adding model 'LoadBalancer'
        db.create_table('dploi_server_loadbalancer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='loadbalancers', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dploi_server', ['LoadBalancer'])

        # Adding model 'Postgres'
        db.create_table('dploi_server_postgres', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='postgress', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default=5432)),
        ))
        db.send_create_signal('dploi_server', ['Postgres'])

        # Adding model 'Gunicorn'
        db.create_table('dploi_server_gunicorn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gunicorns', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dploi_server', ['Gunicorn'])

        # Adding model 'Celery'
        db.create_table('dploi_server_celery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='celerys', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dploi_server', ['Celery'])

        # Adding model 'Redis'
        db.create_table('dploi_server_redis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rediss', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dploi_server', ['Redis'])

        # Adding model 'RabbitMq'
        db.create_table('dploi_server_rabbitmq', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rabbitmqs', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default=5432)),
        ))
        db.send_create_signal('dploi_server', ['RabbitMq'])

        # Adding model 'Solr'
        db.create_table('dploi_server_solr', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='solrs', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default=8983)),
        ))
        db.send_create_signal('dploi_server', ['Solr'])

        # Adding model 'Application'
        db.create_table('dploi_server_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('repository', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal('dploi_server', ['Application'])

        # Adding model 'Deployment'
        db.create_table('dploi_server_deployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='deployments', to=orm['dploi_server.Application'])),
            ('is_live', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('private_key', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('public_key', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('branch', self.gf('django.db.models.fields.CharField')(default='develop', max_length=255)),
        ))
        db.send_create_signal('dploi_server', ['Deployment'])

        # Adding unique constraint on 'Deployment', fields ['application', 'name']
        db.create_unique('dploi_server_deployment', ['application_id', 'name'])

        # Adding model 'DomainName'
        db.create_table('dploi_server_domainname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('dploi_server', ['DomainName'])

        # Adding model 'DomainAlias'
        db.create_table('dploi_server_domainalias', (
            ('domainname_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dploi_server.DomainName'], unique=True, primary_key=True)),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='domain_aliases', to=orm['dploi_server.Deployment'])),
        ))
        db.send_create_signal('dploi_server', ['DomainAlias'])

        # Adding model 'DomainRedirect'
        db.create_table('dploi_server_domainredirect', (
            ('domainname_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dploi_server.DomainName'], unique=True, primary_key=True)),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='domain_redirects', to=orm['dploi_server.Deployment'])),
        ))
        db.send_create_signal('dploi_server', ['DomainRedirect'])

        # Adding model 'PostgresInstance'
        db.create_table('dploi_server_postgresinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['dploi_server.Postgres'])),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='postgres_instances', to=orm['dploi_server.Deployment'])),
            ('alias', self.gf('django.db.models.fields.CharField')(default='default', max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dploi_server', ['PostgresInstance'])

        # Adding unique constraint on 'PostgresInstance', fields ['name', 'service']
        db.create_unique('dploi_server_postgresinstance', ['name', 'service_id'])

        # Adding model 'GunicornInstance'
        db.create_table('dploi_server_gunicorninstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['dploi_server.Gunicorn'])),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gunicorn_instances', to=orm['dploi_server.Deployment'])),
            ('workers', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3)),
            ('max_requests', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2000)),
        ))
        db.send_create_signal('dploi_server', ['GunicornInstance'])

        # Adding model 'RabbitMqInstance'
        db.create_table('dploi_server_rabbitmqinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['dploi_server.RabbitMq'])),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rabbitmq_instances', to=orm['dploi_server.Deployment'])),
            ('virtual_host', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dploi_server', ['RabbitMqInstance'])

        # Adding unique constraint on 'RabbitMqInstance', fields ['virtual_host', 'service']
        db.create_unique('dploi_server_rabbitmqinstance', ['virtual_host', 'service_id'])

        # Adding model 'CeleryInstance'
        db.create_table('dploi_server_celeryinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['dploi_server.Celery'])),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='celery_instances', to=orm['dploi_server.Deployment'])),
            ('workers', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3)),
            ('fire_events', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('beat', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dploi_server', ['CeleryInstance'])

        # Adding model 'RedisInstance'
        db.create_table('dploi_server_redisinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['dploi_server.Redis'])),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='redis_instances', to=orm['dploi_server.Deployment'])),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dploi_server', ['RedisInstance'])

        # Adding model 'SolrInstance'
        db.create_table('dploi_server_solrinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['dploi_server.Solr'])),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='solr_instances', to=orm['dploi_server.Deployment'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dploi_server', ['SolrInstance'])

        # Adding unique constraint on 'SolrInstance', fields ['name', 'service']
        db.create_unique('dploi_server_solrinstance', ['name', 'service_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'SolrInstance', fields ['name', 'service']
        db.delete_unique('dploi_server_solrinstance', ['name', 'service_id'])

        # Removing unique constraint on 'RabbitMqInstance', fields ['virtual_host', 'service']
        db.delete_unique('dploi_server_rabbitmqinstance', ['virtual_host', 'service_id'])

        # Removing unique constraint on 'PostgresInstance', fields ['name', 'service']
        db.delete_unique('dploi_server_postgresinstance', ['name', 'service_id'])

        # Removing unique constraint on 'Deployment', fields ['application', 'name']
        db.delete_unique('dploi_server_deployment', ['application_id', 'name'])

        # Removing unique constraint on 'Host', fields ['realm', 'name']
        db.delete_unique('dploi_server_host', ['realm_id', 'name'])

        # Deleting model 'Realm'
        db.delete_table('dploi_server_realm')

        # Deleting model 'Host'
        db.delete_table('dploi_server_host')

        # Deleting model 'LoadBalancer'
        db.delete_table('dploi_server_loadbalancer')

        # Deleting model 'Postgres'
        db.delete_table('dploi_server_postgres')

        # Deleting model 'Gunicorn'
        db.delete_table('dploi_server_gunicorn')

        # Deleting model 'Celery'
        db.delete_table('dploi_server_celery')

        # Deleting model 'Redis'
        db.delete_table('dploi_server_redis')

        # Deleting model 'RabbitMq'
        db.delete_table('dploi_server_rabbitmq')

        # Deleting model 'Solr'
        db.delete_table('dploi_server_solr')

        # Deleting model 'Application'
        db.delete_table('dploi_server_application')

        # Deleting model 'Deployment'
        db.delete_table('dploi_server_deployment')

        # Deleting model 'DomainName'
        db.delete_table('dploi_server_domainname')

        # Deleting model 'DomainAlias'
        db.delete_table('dploi_server_domainalias')

        # Deleting model 'DomainRedirect'
        db.delete_table('dploi_server_domainredirect')

        # Deleting model 'PostgresInstance'
        db.delete_table('dploi_server_postgresinstance')

        # Deleting model 'GunicornInstance'
        db.delete_table('dploi_server_gunicorninstance')

        # Deleting model 'RabbitMqInstance'
        db.delete_table('dploi_server_rabbitmqinstance')

        # Deleting model 'CeleryInstance'
        db.delete_table('dploi_server_celeryinstance')

        # Deleting model 'RedisInstance'
        db.delete_table('dploi_server_redisinstance')

        # Deleting model 'SolrInstance'
        db.delete_table('dploi_server_solrinstance')


    models = {
        'dploi_server.application': {
            'Meta': {'object_name': 'Application'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'repository': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        'dploi_server.celery': {
            'Meta': {'object_name': 'Celery'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'celerys'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dploi_server.celeryinstance': {
            'Meta': {'object_name': 'CeleryInstance'},
            'beat': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'celery_instances'", 'to': "orm['dploi_server.Deployment']"}),
            'fire_events': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['dploi_server.Celery']"}),
            'workers': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'})
        },
        'dploi_server.deployment': {
            'Meta': {'unique_together': "(('application', 'name'),)", 'object_name': 'Deployment'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployments'", 'to': "orm['dploi_server.Application']"}),
            'branch': ('django.db.models.fields.CharField', [], {'default': "'develop'", 'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'is_live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'private_key': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'public_key': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'dploi_server.domainalias': {
            'Meta': {'object_name': 'DomainAlias', '_ormbases': ['dploi_server.DomainName']},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'domain_aliases'", 'to': "orm['dploi_server.Deployment']"}),
            'domainname_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dploi_server.DomainName']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dploi_server.domainname': {
            'Meta': {'object_name': 'DomainName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'dploi_server.domainredirect': {
            'Meta': {'object_name': 'DomainRedirect', '_ormbases': ['dploi_server.DomainName']},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'domain_redirects'", 'to': "orm['dploi_server.Deployment']"}),
            'domainname_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dploi_server.DomainName']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dploi_server.gunicorn': {
            'Meta': {'object_name': 'Gunicorn'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gunicorns'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dploi_server.gunicorninstance': {
            'Meta': {'object_name': 'GunicornInstance'},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gunicorn_instances'", 'to': "orm['dploi_server.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_requests': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2000'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['dploi_server.Gunicorn']"}),
            'workers': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'})
        },
        'dploi_server.host': {
            'Meta': {'unique_together': "(('realm', 'name'),)", 'object_name': 'Host'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'private_ipv4': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'public_ipv4': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts'", 'to': "orm['dploi_server.Realm']"})
        },
        'dploi_server.loadbalancer': {
            'Meta': {'object_name': 'LoadBalancer'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loadbalancers'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dploi_server.postgres': {
            'Meta': {'object_name': 'Postgres'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postgress'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '5432'})
        },
        'dploi_server.postgresinstance': {
            'Meta': {'unique_together': "(('name', 'service'),)", 'object_name': 'PostgresInstance'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '255'}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postgres_instances'", 'to': "orm['dploi_server.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['dploi_server.Postgres']"}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dploi_server.rabbitmq': {
            'Meta': {'object_name': 'RabbitMq'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rabbitmqs'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '5432'})
        },
        'dploi_server.rabbitmqinstance': {
            'Meta': {'unique_together': "(('virtual_host', 'service'),)", 'object_name': 'RabbitMqInstance'},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rabbitmq_instances'", 'to': "orm['dploi_server.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['dploi_server.RabbitMq']"}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'virtual_host': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dploi_server.realm': {
            'Meta': {'object_name': 'Realm'},
            'base_domain': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'puppet_repository': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'puppet_repository_private_key': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'puppet_repository_public_key': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dploi_server.redis': {
            'Meta': {'object_name': 'Redis'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rediss'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dploi_server.redisinstance': {
            'Meta': {'object_name': 'RedisInstance'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'redis_instances'", 'to': "orm['dploi_server.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['dploi_server.Redis']"})
        },
        'dploi_server.solr': {
            'Meta': {'object_name': 'Solr'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solrs'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '8983'})
        },
        'dploi_server.solrinstance': {
            'Meta': {'unique_together': "(('name', 'service'),)", 'object_name': 'SolrInstance'},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solr_instances'", 'to': "orm['dploi_server.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['dploi_server.Solr']"})
        }
    }

    complete_apps = ['dploi_server']
