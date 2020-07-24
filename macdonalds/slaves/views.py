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
    return render_to_response('subordinates/index.html', locals())
    
def subordinates(request):
    return render_to_response('subordinates/subordinate_list.html', locals())

def mySubordinates(request):
    return render_to_response('subordinates/mySubordinates.html',locals())
    
def myMain(request):
    return render_to_response('subordinates/myMain.html',locals())
    
def buySubordinate(request):
    return render_to_response('subordinates/buySubordinate.html', locals())

def subordinateActions(request):
    return render_to_response('subordinates/buySubordinate.html', locals())
    
def subordinateTrades(request):
    return render_to_response('subordinates/buySubordinate.html', locals())

def         
    
    # 奴隶逃跑    
def subordinateRun(request):
    return render_to_response('subordinates/run.html',locals())
    
    # 折磨
def subordinateAdventure(request):
    return render_to_response('subordinates/adventure.html',locals())
    
    # 释放
def letSubordinateGo(request):
    return render_to_response('subordinates/buySubordinate.html', locals())

    # 更换形象
def changeAvatar(request):
    return render_to_response('subordinates/buySubordinate.html', locals())    

    # 私信
def message(request):
    return render_to_response('subordinates/buySubordinate.html', locals())    
    
    # 看他
def profile(request):
    return render_to_response('subordinates/buySubordinate.html', locals())    

    # 讨好
def flattering(request):
    return render_to_response('subordinates/flattering.html',locals())

    # 赎身
def freedom(request):
    return render_to_response('subordinates/freedom.html',locals())

    # 奴隶竞技
def subordinateAmphitheater(request):
    return render_to_response('subordinates/amphitheater.html',locals())



