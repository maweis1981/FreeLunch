from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SubordinateUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    
class SubordinateRelation(models.Model):
    main = models.ForeignKey(User, related_name='main_set')
    subordinate = models.ForeignKey(User, related_name='subordinate_set')
    