from django.contrib import admin
from tasks.models import Task,Working

class TaskAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Task,TaskAdmin)
