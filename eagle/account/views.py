#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from eagle.account.models import Account
from forms import RegisterForm,LoginForm
import home
 
def index(request):
    return home.home(request)   

def register(request):
    '''注册视图'''
    template_var={}
    form = RegisterForm()    
    if request.method=="POST":
        form=RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user_obj = User.objects.create_user(username,email,password)
            user_obj.save()
	    account = Account(user = user_obj)
	    account.save()		
            _login(request,username,password) #注册完毕 直接登陆
            return HttpResponseRedirect("/account/home/")    
    template_var["form"]=form        
    return render_to_response("account/register.html",template_var,context_instance=RequestContext(request))
    
def login(request):
    '''登陆视图'''
    template_var={}
    form = LoginForm()    
    if request.method == 'POST':
        form=LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request,form.cleaned_data["username"],form.cleaned_data["password"])
            return HttpResponseRedirect("/account/home/")
    template_var["form"]=form        
    return render_to_response("account/login.html",template_var,context_instance=RequestContext(request))
    
def _login(request,username,password):
    '''登陆核心方法'''
    ret=False
    user=authenticate(username=username,password=password)
    if user:
        if user.is_active:
            auth_login(request,user)
            ret=True
        else:
            messages.add_message(request, messages.INFO, _(u'用户没有激活'))
    else:
        messages.add_message(request, messages.INFO, _(u'用户不存在'))
    return ret
    
def logout(request):
    '''注销视图'''
    auth_logout(request)
    return HttpResponseRedirect('/account/login/')
