#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from account.models import Account
from task import models as task_model
import datetime

from account.models import Account



def fetch_lists(user_id):
    day_task, week_task, month_task, year_task, task_done = [], [], [], [], []
    all_tasks = task_model.Task.objects.filter(owner=user_id)
    for task_item in all_tasks:
        if task_item.mode == task_model.ONCE_TASK:
            if task_item.is_done():
                task_done.append(task_item)
            elif not task_item.is_expired() and task_model.in_today(task_item):
                day_task.append(task_item)
        elif task_item.mode == task_model.DAY_TASK:
            if task_item.is_done():
                task_done.append(task_item)
            if not task_item.is_expired():
                day_task.append(task_item)
        elif task_item.mode == task_model.WEEK_TASK:
            if task_item.is_done():
                task_done.append(task_item)
            elif not task_item.is_expired():
                week_task.append(task_item)
        elif task_item.mode == task_model.MONTH_TASK:
            if task_item.is_done():
                task_done.append(task_item)
            elif not task_item.is_expired():
                month_task.append(task_item)
        elif year_task.mode == task_model.YEAR_TASK:
            if task_item.is_done():
                task_done.append(task_item)
            elif not task_item.is_expired():
                year_task.append(task_item)
    return day_task, week_task, month_task, year_task, task_done                



def home(request):
    account = Account.objects.get(user=request.user)
    day_task, week_task, month_task, year_task, task_done = fetch_lists(
        account.id)
    #print day_task, week_task, month_task, year_task, task_done
    
    tasks_list = {"day":day_task,
                  "week":week_task,
                  "month":month_task,
                  "year":year_task,
                  "done":task_done}

    return render_to_response('common/index.html',
                              {"tasks_list":tasks_list},
                              context_instance=RequestContext(request))
