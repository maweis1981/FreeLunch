from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404,HttpResponse

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserProfile
from accounts.forms import UserProfileForm

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse

from decimal import *
import settings
import simplejson as json

def reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return HttpResponseRedirect(reverse("my",args=()))
        else:
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render_to_response('regist.html', locals())

# register with username and password1 password2
def regUser(request):
    # 注册 post username and password1 and password2 to create a new user
    return render_to_response('regist.html', locals())
    
def login(request):
    # login 
    return render_to_response('regist.html', locals())

def loginViaWeibo(request):
    return render_to_response('regist.html', locals())
    
def loginViaQQ(request):
    return render_to_response('regist.html', locals())
    
    # get user info: username and bonus number
def userInfo(request):
    # username and user's bonus number and level.
    return render_to_response('regist.html', locals())