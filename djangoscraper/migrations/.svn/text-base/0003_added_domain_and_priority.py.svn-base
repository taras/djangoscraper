
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Task.priority'
        db.add_column('scraper_task', 'priority', models.FloatField())
        
        # Adding field 'Task.domain'
        db.add_column('scraper_task', 'domain', models.CharField(max_length=255))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Task.priority'
        db.delete_column('scraper_task', 'priority')
        
        # Deleting field 'Task.domain'
        db.delete_column('scraper_task', 'domain')
        
    
    
    models = {
        'scraper.task': {
            'args': ('PickledObjectField', [], {}),
            'callback': ('models.CharField', [], {'max_length': '255'}),
            'completed': ('models.BooleanField', [], {'default': '0'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'domain': ('models.CharField', [], {'max_length': '255'}),
            'errors': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('models.CharField', [], {'max_length': '255'}),
            'locked': ('models.BooleanField', [], {'default': '0'}),
            'priority': ('models.FloatField', [], {}),
            'result': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
