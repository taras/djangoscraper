from django.contrib import admin
from djangoscraper.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('domain', 'name', 'priority', 'completed', 'locked', 'created')
    list_filter = ('domain', 'priority', 'completed', 'name')
    ordering = ['priority', 'created']
    search_fields = ('description', 'name', 'errors')

admin.site.register(Task, TaskAdmin)