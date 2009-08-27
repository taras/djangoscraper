
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
    
    
    models = {
        'scraper.task': {
            'args': ('PickledObjectField', [], {}),
            'callback': ('models.CharField', [], {'max_length': '255'}),
            'completed': ('models.BooleanField', [], {'default': '0'}),
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'errors': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('models.CharField', [], {'max_length': '255'}),
            'locked': ('models.BooleanField', [], {'default': '0'}),
            'result': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['scraper']
