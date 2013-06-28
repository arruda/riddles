# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Riddle'
        db.create_table(u'riddles_riddle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('riddles', ['Riddle'])


    def backwards(self, orm):
        # Deleting model 'Riddle'
        db.delete_table(u'riddles_riddle')


    models = {
        'riddles.riddle': {
            'Meta': {'object_name': 'Riddle'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['riddles']