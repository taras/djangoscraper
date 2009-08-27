
from south.db import db
from django.db import models
from scraper.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Task'
        db.create_table('scraper_task', (
            ('errors', models.TextField()),
            ('locked', models.BooleanField(default=0)),
            ('description', models.TextField()),
            ('created', models.DateTimeField(auto_now_add=True)),
            ('completed', models.BooleanField(default=0)),
            ('args', PickledObjectField()),
            ('callback', models.CharField(max_length=255)),
            ('result', models.TextField()),
            ('identifier', models.CharField(max_length=255)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('scraper', ['Task'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Task'
        db.delete_table('scraper_task')
        
    
    
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
