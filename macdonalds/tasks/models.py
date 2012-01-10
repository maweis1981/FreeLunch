from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):
    creater = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    task_link = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.title)
    
class Working(models.Model):
    task = models.ForeignKey(Task)
    worker = models.ForeignKey(User)
    status = models.IntegerField()
    worked_date = models.DateTimeField(auto_now_add=True)
    
