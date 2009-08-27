
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Task.name'
        db.add_column('scraper_task', 'name', models.CharField(max_length=255))
        
        # Deleting field 'Task.callback'
        db.delete_column('scraper_task', 'callback')
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Task.name'
        db.delete_column('scraper_task', 'name')
        
        # Adding field 'Task.callback'
        db.add_column('scraper_task', 'callback', models.CharField(max_length=255))
        
    
    
    models = {
        'scraper.task': {
            'args': ('PickledObjectField', [], {}),
            'completed': ('models.BooleanField', [], {'default': '0'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'domain': ('models.CharField', [], {'max_length': '255'}),
            'errors': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('models.CharField', [], {'max_length': '255'}),
            'locked': ('models.BooleanField', [], {'default': '0'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'priority': ('models.FloatField', [], {'default': '0.0'}),
            'result': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
