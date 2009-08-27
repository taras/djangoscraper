
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Task.errors'
        db.alter_column('scraper_task', 'errors', models.TextField(blank=True))
        
        # Changing field 'Task.description'
        db.alter_column('scraper_task', 'description', models.TextField(blank=True))
        
        # Changing field 'Task.args'
        db.alter_column('scraper_task', 'args', PickledObjectField(blank=True))
        
        # Changing field 'Task.result'
        db.alter_column('scraper_task', 'result', models.TextField(blank=True))
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Task.errors'
        db.alter_column('scraper_task', 'errors', models.TextField())
        
        # Changing field 'Task.description'
        db.alter_column('scraper_task', 'description', models.TextField())
        
        # Changing field 'Task.args'
        db.alter_column('scraper_task', 'args', PickledObjectField())
        
        # Changing field 'Task.result'
        db.alter_column('scraper_task', 'result', models.TextField())
        
    
    
    models = {
        'scraper.task': {
            'args': ('PickledObjectField', [], {'blank': 'True'}),
            'completed': ('models.BooleanField', [], {'default': '0'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'blank': 'True'}),
            'domain': ('models.CharField', [], {'max_length': '255'}),
            'errors': ('models.TextField', [], {'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'locked': ('models.BooleanField', [], {'default': '0'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'priority': ('models.FloatField', [], {'default': '0.0'}),
            'result': ('models.TextField', [], {'blank': 'True'}),
            'start_urls': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
