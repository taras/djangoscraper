
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Task.priority'
        db.alter_column('scraper_task', 'priority', models.FloatField(default=0.0))
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Task.priority'
        db.alter_column('scraper_task', 'priority', models.FloatField())
        
    
    
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
            'priority': ('models.FloatField', [], {'default': '0.0'}),
            'result': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
