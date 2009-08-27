
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting field 'Task.errors'
        db.delete_column('scraper_task', 'errors')
        
        # Deleting field 'Task.result'
        db.delete_column('scraper_task', 'result')
        
    
    
    def backwards(self, orm):
        
        # Adding field 'Task.errors'
        db.add_column('scraper_task', 'errors', models.TextField(blank=True))
        
        # Adding field 'Task.result'
        db.add_column('scraper_task', 'result', models.TextField(blank=True))
        
    
    
    models = {
        'scraper.task': {
            'args': ('PickledObjectField', [], {'blank': 'True'}),
            'completed': ('models.BooleanField', [], {'default': '0'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'blank': 'True'}),
            'domain': ('models.CharField', [], {'max_length': '255'}),
            'finish': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'locked': ('models.BooleanField', [], {'default': '0'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'priority': ('models.FloatField', [], {'default': '0.0'}),
            'start': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_urls': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
