# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field likers on 'Photo'
        db.delete_table(db.shorten_name('photo_likers'))


    def backwards(self, orm):
        # Adding M2M table for field likers on 'Photo'
        m2m_table_name = db.shorten_name('photo_likers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm['space.photo'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photo_id', 'user_id'])


    models = {
        'space.photo': {
            'Meta': {'ordering': "('-created_time',)", 'object_name': 'Photo', 'db_table': "'photo'"},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'photo_album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['space.PhotoAlbum']"}),
            'thumbs_file': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'space.photoalbum': {
            'Meta': {'ordering': "('-created_time',)", 'object_name': 'PhotoAlbum', 'db_table': "'photo_album'"},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['space']