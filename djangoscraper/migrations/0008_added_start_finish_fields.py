
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Task.start'
        db.add_column('scraper_task', 'start', models.DateTimeField(null=True, blank=True))
        
        # Adding field 'Task.finish'
        db.add_column('scraper_task', 'finish', models.DateTimeField(null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Task.start'
        db.delete_column('scraper_task', 'start')
        
        # Deleting field 'Task.finish'
        db.delete_column('scraper_task', 'finish')
        
    
    
    models = {
        'scraper.task': {
            'args': ('PickledObjectField', [], {'blank': 'True'}),
            'completed': ('models.BooleanField', [], {'default': '0'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'blank': 'True'}),
            'domain': ('models.CharField', [], {'max_length': '255'}),
            'errors': ('models.TextField', [], {'blank': 'True'}),
            'finish': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'locked': ('models.BooleanField', [], {'default': '0'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'priority': ('models.FloatField', [], {'default': '0.0'}),
            'result': ('models.TextField', [], {'blank': 'True'}),
            'start': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_urls': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
