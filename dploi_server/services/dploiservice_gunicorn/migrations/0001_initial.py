# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Gunicorn'
        db.create_table('dploiservice_gunicorn_gunicorn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gunicorns', to=orm['dploi_server.Host'])),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dploiservice_gunicorn', ['Gunicorn'])

        # Adding model 'GunicornInstance'
        db.create_table('dploiservice_gunicorn_gunicorninstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deployment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gunicorninstances', to=orm['dploi_server.Deployment'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['dploiservice_gunicorn.Gunicorn'])),
            ('workers', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3)),
            ('max_requests', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2000)),
        ))
        db.send_create_signal('dploiservice_gunicorn', ['GunicornInstance'])


    def backwards(self, orm):
        
        # Deleting model 'Gunicorn'
        db.delete_table('dploiservice_gunicorn_gunicorn')

        # Deleting model 'GunicornInstance'
        db.delete_table('dploiservice_gunicorn_gunicorninstance')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dploi_server.application': {
            'Meta': {'object_name': 'Application'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'repository': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
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
        'dploi_server.host': {
            'Meta': {'object_name': 'Host'},
            'administrator_groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dploi_admins'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'host_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dploi_server.HostType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'private_ipv4': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'public_ipv4': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'realm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts'", 'to': "orm['dploi_server.Realm']"})
        },
        'dploi_server.hosttype': {
            'Meta': {'object_name': 'HostType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dploi_server.HostType']", 'null': 'True', 'blank': 'True'}),
            'puppet_classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dploi_server.PuppetClass']", 'symmetrical': 'False'})
        },
        'dploi_server.loadbalancer': {
            'Meta': {'object_name': 'LoadBalancer'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loadbalancers'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dploi_server.puppetclass': {
            'Meta': {'object_name': 'PuppetClass'},
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'dploiservice_gunicorn.gunicorn': {
            'Meta': {'object_name': 'Gunicorn'},
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gunicorns'", 'to': "orm['dploi_server.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dploiservice_gunicorn.gunicorninstance': {
            'Meta': {'object_name': 'GunicornInstance'},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gunicorninstances'", 'to': "orm['dploi_server.Deployment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_requests': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2000'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['dploiservice_gunicorn.Gunicorn']"}),
            'workers': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'})
        }
    }

    complete_apps = ['dploiservice_gunicorn']
