from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SlaveUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    
class SlaveRelation(models.Model):
    master = models.ForeignKey(User, related_name='master_set')
    slave = models.ForeignKey(User, related_name='slave_set')
    