# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'RedisInstance.port'
        db.add_column('dploi_server_redisinstance', 'port', self.gf('django.db.models.fields.IntegerField')(default=50000), keep_default=False)

        # Adding unique constraint on 'RedisInstance', fields ['port', 'service']
        db.create_unique('dploi_server_redisinstance', ['port', 'service_id'])

        # Adding field 'Deployment.load_balancer'
        db.add_column('dploi_server_deployment', 'load_balancer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='deployments', null=True, to=orm['dploi_server.LoadBalancer']), keep_default=False)


    def backwards(self, orm):
        
        # Removing unique constraint on 'RedisInstance', fields ['port', 'service']
        db.delete_unique('dploi_server_redisinstance', ['port', 'service_id'])

        # Deleting field 'RedisInstance.port'
        db.delete_column('dploi_server_redisinstance', 'port')

        # Deleting field 'Deployment.load_balancer'
        db.delete_column('dploi_server_deployment', 'load_balancer_id')


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
            'load_balancer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'deployments'", 'null': 'True', 'to': "orm['dploi_server.LoadBalancer']"}),
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
            'Meta': {'unique_together': "(('service', 'port'),)", 'object_name': 'RedisInstance'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'redis_instances'", 'to': "orm['dploi_server.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {}),
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
