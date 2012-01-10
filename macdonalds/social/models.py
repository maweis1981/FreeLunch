from django.db import models

from django.contrib.auth.models import User

class WeiboAccessToken(models.Model):
    user = models.ForeignKey(User)
    screen_name = models.CharField(max_length=256)
    access_token = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    
    def __unicode__(self):
        return '%s,%s' % (self.user.username,self.screen_name)
        
class InviteCode(models.Model):
    master = models.ForeignKey(User)
    invite_code = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)
    
class Relatives(models.Model):
    r_user = models.ForeignKey(User,related_name='r_relative_users_set')
    r_master = models.ForeignKey(User,related_name='r_relative_master_set')
    create_date = models.DateTimeField(auto_now_add=True)    