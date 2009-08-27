
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Task.start_urls'
        db.add_column('scraper_task', 'start_urls', models.TextField())
        
        # Deleting field 'Task.identifier'
        db.delete_column('scraper_task', 'identifier')
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Task.start_urls'
        db.delete_column('scraper_task', 'start_urls')
        
        # Adding field 'Task.identifier'
        db.add_column('scraper_task', 'identifier', models.CharField(max_length=255))
        
    
    
    models = {
        'scraper.task': {
            'args': ('PickledObjectField', [], {}),
            'completed': ('models.BooleanField', [], {'default': '0'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'domain': ('models.CharField', [], {'max_length': '255'}),
            'errors': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'locked': ('models.BooleanField', [], {'default': '0'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'priority': ('models.FloatField', [], {'default': '0.0'}),
            'result': ('models.TextField', [], {}),
            'start_urls': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
