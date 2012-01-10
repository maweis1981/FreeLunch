#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Peter Ma on 2012-01-05.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django.contrib import admin
from social.models import WeiboAccessToken

class WeiboAccessTokenAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(WeiboAccessToken,WeiboAccessTokenAdmin)
