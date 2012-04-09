#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
from task import models as task_model
import collections;
import datetime
import calendar

def fetch_lists(user_id):
    tag_task, day_task, week_task, month_task, over_month_task, task_record = [], [], [], [], [], []
    ''' xx_task contains tasks *must* to be done in xx'''
    all_tasks = task_model.Task.objects.filter(owner=user_id)
    cur_date = datetime.datetime.now()
    for task_item in all_tasks:
        if not task_item.alive:
            continue
        if task_item.done():
            task_record.append(task_item)
            ''' not suitable!!! TODO'''
            continue
        if False and not task_item.active():
            '''not in use!!!'''
            task_record.insert(0, task_item)
            ''' overdue tasks'''
        elif task_item.mode == task_model.TAG_TASK:
            tag_task.append(task_item)
        elif task_item.mode == task_model.ONCE_TASK:
            print '~~~in-once-task~~~', task_item
            delt_year = task_item.begin_time.year - cur_date.year
            delt_month = task_item.begin_time.month - cur_date.month
            delt_weekday = task_item.begin_time.weekday() - cur_date.weekday()
            delt_day = (task_item.begin_time - cur_date).days

            if delt_year > 0 or delt_month > 0:
                over_month_task.append(task_item)
            elif delt_day > delt_weekday:
                month_task.append(task_item)
            elif delt_day > 0:
                week_task.append(task_item)
            else:
                day_task.append(task_item)
        elif task_item.mode == task_model.DAY_TASK:
            print '~~~in-day-task~~~', task_item
            day_task.append(task_item)
        elif task_item.mode == task_model.WEEK_TASK: 
            print '~~~in-week-task~~~', task_item
            if cur_date.weekday() == 6:
                '''the last day of the week, so the task must be done today'''
                day_task.append(task_item)
            else:
                week_task.append(task_item)
        elif task_item.mode == task_model.MONTH_TASK:
            print '~~~in-month-task~~~', task_item
            max_month_day = calendar.monthrange(cur_date.year, cur_date.month)[1]
            last_month_day = datetime.datetime(cur_date.year, cur_date.month, max_month_day)
            if cur_date.day == max_month_day:
                day_task.append(task_item)
            elif max_month_day - cur_date.day > last_month_day.weekday() - cur_date.weekday():
                month_task.append(task_item)
            else:
                '''the last week of the month, so the task must be done today'''
                week_task.append(task_item)
        else:
            ''' simplified with error '''
            over_month_task.append(task_item)

    return tag_task, day_task, week_task, month_task, over_month_task, task_record             

def home(request):
    account = Account.objects.get(user=request.user) 
    tag_task, day_task, week_task, month_task, over_month_task, task_record = fetch_lists(
        account.id)
    #print day_task, week_task, month_task, year_task, task_done
    
    tasks_list = {"on today": day_task,
                  "in this week": week_task,
                  "in this month": month_task,
                  "over a month": over_month_task,
                  "records": task_record}

    print '-----------------------------'
    for key, value in tasks_list.items():
        print key,value
    print '-----------------------------'
    
    priority = {"on today": 1,
                "in this week": 2,
                "in this month": 3,
                "over a month": 4,
                "records": 5}
    ordered_tasks_list = collections.OrderedDict(sorted(tasks_list.items(), key=lambda t: priority[t[0]]))
    return render_to_response("common/index.html",
                              {"tasks_list": ordered_tasks_list,
                               "tag_tasks":tag_task},
                              context_instance=RequestContext(request))
