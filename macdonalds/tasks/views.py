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

# load all tasks
def index(request):
    tasks = Task.objects.all()
    return render_to_response('tasks/index.html', locals())
    
def doingTasks(request):
    return render_to_response('tasks/doing.html', locals())
    
def doneTasks(request):
    return render_to_response('tasks/done.html',locals())
    
def loadTaskById(request):
    return render_to_response('tasks/task.html',locals())
    
    # 标记任务完成
def markTaskDone(request):
    return render_to_response('tasks/markTaskDone.html',locals())