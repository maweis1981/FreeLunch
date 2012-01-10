#!/usr/bin/env python
# encoding: utf-8
"""
testWeibo.py

Created by Peter Ma on 2012-01-04.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from weibo import APIClient
import simplejson as json

def main():
    APP_KEY = '3331857532' # app key
    APP_SECRET = '0a965b08dd9754165e5fa98348e15959' # app secret
    CALLBACK_URL = 'http://maweis.com/callback' # callback url
    
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    print url

def loadUserId():
    uidStr = "%s" % {'uid': 1644398682}
    print uidStr
    ids = json.loads(uidStr)
    print uidStr
    print ids['uid']
    
    

if __name__ == '__main__':
	loadUserId()

