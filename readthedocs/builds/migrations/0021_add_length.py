# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Build.length'
        db.add_column(u'builds_build', 'length',
                      self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Build.length'
        db.delete_column(u'builds_build', 'length')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'builds.build': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Build'},
            'commit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'exit_code': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'output': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'builds'", 'to': u"orm['projects.Project']"}),
            'setup': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'setup_error': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'finished'", 'max_length': '55'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '55'}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'builds'", 'null': 'True', 'to': u"orm['builds.Version']"})
        },
        u'builds.version': {
            'Meta': {'ordering': "['-verbose_name']", 'unique_together': "[('project', 'slug')]", 'object_name': 'Version'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'built': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'machine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'privacy_level': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '20'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'versions'", 'to': u"orm['projects.Project']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'supported': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '20'}),
            'uploaded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'builds.versionalias': {
            'Meta': {'object_name': 'VersionAlias'},
            'from_slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aliases'", 'to': u"orm['projects.Project']"}),
            'to_slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.project': {
            'Meta': {'ordering': "('slug',)", 'object_name': 'Project'},
            'analytics_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'canonical_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'conf_py_file': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'default_branch': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_version': ('django.db.models.fields.CharField', [], {'default': "'latest'", 'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'django_packages_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'documentation_type': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '20'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '20'}),
            'main_language_project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            'mirror': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num_major': ('django.db.models.fields.IntegerField', [], {'default': '2', 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'num_minor': ('django.db.models.fields.IntegerField', [], {'default': '2', 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'num_point': ('django.db.models.fields.IntegerField', [], {'default': '2', 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'privacy_level': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '20'}),
            'programming_language': ('django.db.models.fields.CharField', [], {'default': "'words'", 'max_length': '20', 'blank': 'True'}),
            'project_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'python_interpreter': ('django.db.models.fields.CharField', [], {'default': "'python'", 'max_length': '20'}),
            'related_projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['projects.Project']", 'null': 'True', 'through': u"orm['projects.ProjectRelationship']", 'blank': 'True'}),
            'repo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'repo_type': ('django.db.models.fields.CharField', [], {'default': "'git'", 'max_length': '10'}),
            'requirements_file': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'single_version': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'suffix': ('django.db.models.fields.CharField', [], {'default': "'.rst'", 'max_length': '10'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'}),
            'use_system_packages': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_virtualenv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'version_privacy_level': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '20'})
        },
        u'projects.projectrelationship': {
            'Meta': {'object_name': 'ProjectRelationship'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'superprojects'", 'to': u"orm['projects.Project']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subprojects'", 'to': u"orm['projects.Project']"})
        }
    }

    complete_apps = ['builds']