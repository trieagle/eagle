#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.htpp import HttpResponseRedirect
from django.template import RequestContext
from task import models as task_model
import datetime



def fetch_lists(user_id):
    day_task, week_task, month_task, year_task, task_done = [], [], [], [], []
    all_tasks = task_model.task.objects.filter(task_onwer=user_id)
    #很糟糕的代码呢，能以多态的方式重构码？
    for task_item in all_tasks:
        if task_item.mode == task_model.ONCE_TASK:
            if task_item.is_done():
                day_task.push(task_item)
            elif not task_item.is_expired() and task_model.in_today(task_item):
                task_done.push(task_item)
        elif task_item.mode == task_model.DAY_TASK:
            if task_item.is_done():
                task_done.push(task_item)
            if not task_item.is_expired():
                day_task.push(task_item)
        elif task_item.mode == task_model.WEEK_TASK:
            if task_item.is_done():
                task_done.push(task_item)
            elif not task_item.is_expired():
                week_task.push(task_item)
        elif task_item.mode == task_model.MONTH_TASK:
            if task_item.is_done():
                task_done.push(task_item)
            elif not task_item.is_expired():
                month_task.push(task_item)
        elif year_task.mode == task_model.YEAR_TASK:
            if task_item.is_done():
                task_done.push(task_item)
            elif not task_item.is_expired():
                year_task.push(task_item)
    return day_task, week_task, month_task, year_task, task_done                



def home(request):
    if not request.user.is_authenticated():
        return render_to_response('login.html',
                                  {},
                                  context_instance=RequestContext(request))
    day_task, week_task, month_task, year_task, task_done = fetch_lists(
        request.user.id)
    

        
