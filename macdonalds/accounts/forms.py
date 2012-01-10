#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Peter Ma on 2012-01-05.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""
from django import forms
from accounts.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user')

    def save(self,user_id,commit=True):
        userProfile = super(UserProfileForm,self).save(commit=False)
        userProfile.set_user_id(user_id)
        if commit:
            userProfile.save()
        return userProfile
