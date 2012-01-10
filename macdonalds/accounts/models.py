#!/usr/bin/env python
# encoding: utf-8


from django.db import models,connection
from django.contrib.auth.models import User,UserManager

class UserProfile(models.Model):

    GENDER_CHOICES = (
    (1, '男'),
    (2, '女'),
    )

    PROVINCE_CHOICES = (
    ('JiangSu','江苏'),
    ('ShangHai','上海'),
    )

    user = models.ForeignKey(User, unique=True)
    gender = models.IntegerField(max_length=1, choices=GENDER_CHOICES,default=1)
    birthday = models.DateField(blank=True,null=True)
    province = models.CharField(max_length=20, choices=PROVINCE_CHOICES,default=1)
    city = models.CharField(max_length=10)
    livecity = models.CharField(max_length=10)
    regist_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username

    def set_user_id(self,raw_user_id):
        raw_user = User.objects.get(pk = raw_user_id)
        if raw_user:
            self.user = raw_user
        else:
            raise Exception('User not exist')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])