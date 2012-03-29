#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
from task import models as task_model

def fetch_lists(user_id):
    day_task, week_task, month_task, year_task, task_done = [], [], [], [], []
    task_type = {task_model.ONCE_TASK: day_task,
                 task_model.DAY_TASK: day_task,
                 task_model.WEEK_TASK: week_task,
                 task_model.MONTH_TASK: month_task,
                 task_model.YEAR_TASK: year_task}

    all_tasks = task_model.Task.objects.filter(owner=user_id)

    for task_item in all_tasks:
        task_list = task_type[task_item.mode]
        if task_item.done():
            task_done.append(task_item)
        elif task_item.active() or \
                (task_item.mode == task_model.ONCE_TASK and 
                 task_model.in_today(task_item)):
            task_list.append(task_item)
    return day_task, week_task, month_task, year_task, task_done                

def home(request):
    account = Account.objects.get(user=request.user)
    day_task, week_task, month_task, year_task, task_done = fetch_lists(
        account.id)
    #print day_task, week_task, month_task, year_task, task_done
    
    tasks_list = {"day": day_task,
                  "week": week_task,
                  "month": month_task,
                  "year": year_task,
                  "done": task_done}

    return render_to_response('common/index.html',
                              {"tasks_list": tasks_list},
                              context_instance=RequestContext(request))
