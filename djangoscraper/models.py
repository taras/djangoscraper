from django.db import models
from djangoscraper.fields.pickled import PickledObjectField

class Task(models.Model):
    domain = models.CharField(max_length=255)
    name = models.CharField(max_length=255)    
    start_urls = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    priority = models.FloatField(default=0.0)
    args = PickledObjectField(blank=True)
    locked = models.BooleanField(default=0)
    completed = models.BooleanField(default=0)
    start = models.DateTimeField(blank=True, null=True)
    finish = models.DateTimeField(blank=True, null=True)
    
    def lock(self):
        self.locked = 1
        self.save()
    
    def complete(self):
        self.completed = 1
        self.save()
        
    def next(self, **kwargs):
        qs = Task.objects.filter(**kwargs).order_by('priority')
        if qs:
            return qs[0]
        else:
            return None
        
    def load(self,id):
        return self.next(id=id)