#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Peter Ma on 2012-01-04.
Copyright (c) 2012 __Maven Studio__. All rights reserved.
Created On 4 Jan, 2012 1:54 PM
At Nanjing Home.
"""
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from sinaweibo.weibo import APIClient
from django.shortcuts import redirect,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from macdonalds import settings
from django.template import Context, loader
from models import WeiboAccessToken
import simplejson as json
from django.contrib.auth.models import User

import math
import random

from django.core.cache import cache

def index(request):
    title = 'weibo validate btn'
    return render_to_response('social/index.html', locals())
     
def weiboValidate(request):
    client = APIClient(app_key=settings.APP_KEY, app_secret=settings.APP_SECRET, redirect_uri=settings.CALLBACK_URL)
    url = client.get_authorize_url()
    print url
    return HttpResponseRedirect('%s' % url)
    

def callback(request):
    code = request.GET['code']
    client = APIClient(app_key=settings.APP_KEY, app_secret=settings.APP_SECRET, redirect_uri=settings.CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in
    # TODO: needs to store access token in the database and memcache.
    cache.set('access_token',access_token,expires_in)
    cache.set('expires_in',expires_in,expires_in)
    #参数分别为key,value,超时时间
    client.set_access_token(access_token, expires_in)
    user = client.get.users__show(uid=client.get.account__get_uid().uid)
    
    weiboToken = WeiboAccessToken()
    weiboToken.user = request.user
    weiboToken.screen_name = user.screen_name
    weiboToken.access_token = access_token
    weiboToken.save()
    
    return render_to_response('social/user.html',locals())
        
def updateUserInfo(request):
    if request.method == 'POST':
        user = User()
        # TODO check the username exist?
        user.username = request.POST['username']
        exists = User.objects.filter(username=user.username)
        if  len(exists) > 0:
            return HttpResponse('User Name Exist!',status=401)

        if request.POST['password1'] == request.POST['password2']:
            user.set_password(request.POST['password1'])
        user.save()
        return render_to_response('social/user_info.html')
        
def loadFriendsFromWeibo(request):
    client = APIClient(app_key=settings.APP_KEY, app_secret=settings.APP_SECRET, redirect_uri=settings.CALLBACK_URL)
    access_token = cache.get('access_token')
    expires_in = cache.get('expires_in')
    client.set_access_token(access_token,expires_in)
    print access_token
    print expires_in
    client.post.statuses__update(status=u'test %s' % random.random())
    
    friends = client.get.friendships__friends__bilateral()
    # return HttpResponse('access token is %s' % access_token)
    return render_to_response('social/friends.html',locals())    
        

def weiboAccessToken(request):
    print request.GET
    return HttpResponse(request.GET)
    # code = request.GET['code']
    # client = APIClient(app_key=settings.APP_KEY, app_secret=settings.APP_SECRET, redirect_uri=settings.CALLBACK_URL)
    # r = client.request_access_token(code)
    # access_token = r.access_token
    # expires_in = r.expires_in
    # # TODO: needs to store access token in the database and memcache.
    # print access_token
    # print expires_in
    # client.set_access_token(access_token, expires_in)
    # print client.upload.statuses__upload(status=u'一起来免费午餐', pic=open('/Volumes/HDD/Pictures/logo.png'))
    # return HttpResponse('%s %s',access_token,expires_in)
    