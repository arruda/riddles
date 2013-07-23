# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guess.riddle'
        db.add_column(u'riddles_guess', 'riddle',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riddles.Riddle'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Guess.riddle'
        db.delete_column(u'riddles_guess', 'riddle_id')


    models = {
        u'riddles.guess': {
            'Meta': {'object_name': 'Guess'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'riddle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riddles.Riddle']", 'null': 'True'})
        },
        'riddles.riddle': {
            'Meta': {'object_name': 'Riddle'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['riddles']