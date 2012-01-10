#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Peter Ma on 2012-01-04.
Copyright (c) 2012 Maven Studio. All rights reserved.
Created On 6 Jan, 2012 11:06 PM
At Nanjing Home.
"""
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import redirect,render_to_response
from django.http import HttpResponseRedirect, HttpResponse

from macdonalds import settings
from django.template import Context, loader
from models import Task
import simplejson as json
from django.contrib.auth.models import User

from django.core.cache import cache

def index(request):
    return render_to_response('slaves/index.html', locals())
    
def slaves(request):
    return render_to_response('slaves/slave_list.html', locals())

def mySlaves(request):
    return render_to_response('slaves/mySlaves.html',locals())
    
def myMaster(request):
    return render_to_response('slaves/myMaster.html',locals())
    
def buySlave(request):
    return render_to_response('slaves/buySlave.html', locals())

def slaveActions(request):
    return render_to_response('slaves/buySlave.html', locals())
    
def slaveTrades(request):
    return render_to_response('slaves/buySlave.html', locals())

def         
    
    # 奴隶逃跑    
def slaveRun(request):
    return render_to_response('slaves/run.html',locals())
    
    # 折磨
def slaveAdventure(request):
    return render_to_response('slaves/adventure.html',locals())
    
    # 释放
def letSlaveGo(request):
    return render_to_response('slaves/buySlave.html', locals())

    # 更换形象
def changeAvatar(request):
    return render_to_response('slaves/buySlave.html', locals())    

    # 私信
def message(request):
    return render_to_response('slaves/buySlave.html', locals())    
    
    # 看他
def profile(request):
    return render_to_response('slaves/buySlave.html', locals())    

    # 讨好
def flattering(request):
    return render_to_response('slaves/flattering.html',locals())

    # 赎身
def freedom(request):
    return render_to_response('slaves/freedom.html',locals())

    # 奴隶竞技
def slaveAmphitheater(request):
    return render_to_response('slaves/amphitheater.html',locals())



