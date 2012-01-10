#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Peter Ma on 2012-01-05.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views',
    url(r'^reg$', 'reg', name='reg'),
    url(r'^profile$', 'my', name='my'),
    url(r'^space/(?P<user_id>\d+)/$', 'space', name='space'),
    url(r'^edit$', 'edit', name='edit'),
)