#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
from task import models as task_model
import collections;
import datetime
import calendar

COLL_TAG, COLL_DAY, COLL_WEEK, COLL_MONTH, COLL_OVER_MONTH, COLL_RECORD = range(6)

def get_task_coll(task):
    if not task_item.alive:
        continue
    if task_item.done():
        return COLL_RECORD
        ''' not suitable!!! TODO'''
        continue
    if False and not task_item.active():
        return COLL_RECORD
        '''not in use!!!'''
        ''' overdue tasks'''
    elif task_item.mode == task_model.TAG_TASK:
        return COLL_TAG
    elif task_item.mode == task_model.ONCE_TASK:
        print '~~~in-once-task~~~', task_item
        delt_year = task_item.begin_time.year - cur_date.year
        delt_month = task_item.begin_time.month - cur_date.month
        delt_weekday = task_item.begin_time.weekday() - cur_date.weekday()
        delt_day = (task_item.begin_time - cur_date).days

        if delt_year > 0 or delt_month > 0:
            return COLL_OVER_MONTH
        elif delt_day > delt_weekday:
            return COLL_MONTH
        elif delt_day > 0:
            return COLL_WEEK
        else:
            return COLL_DAY

    elif task_item.mode == task_model.DAY_TASK:
        print '~~~in-day-task~~~', task_item
        return COLL_DAY
    elif task_item.mode == task_model.WEEK_TASK: 
        print '~~~in-week-task~~~', task_item
        if cur_date.weekday() == 6:
        '''the last day of the week, so the task must be done today'''
            return COLL_DAY
        else:
            return COLL_WEEK
    elif task_item.mode == task_model.MONTH_TASK:
        print '~~~in-month-task~~~', task_item
        max_month_day = calendar.monthrange(cur_date.year, cur_date.month)[1]
        last_month_day = datetime.datetime(cur_date.year, cur_date.month, max_month_day)
        if cur_date.day == max_month_day:
            return COLL_DAY
        elif max_month_day - cur_date.day > last_month_day.weekday() - cur_date.weekday():
            return COLL_MONTH
        else:
            '''the last week of the month, so the task must be done today'''
            return COLL_WEEK
    else:
        ''' simplified with error '''
        return COLL_OVER_MONTH

def fetch_lists(user_id):
    ''' xx_task contains tasks *must* to be done in xx'''
    task_dict = { "in tag": [],
                  "on today": [],
                  "in this week": [],
                  "in this month": [],
                  "over a month": [],
                  "records": []}
    all_tasks = task_model.Task.objects.filter(owner=user_id)
    cur_date = datetime.datetime.now()
    for task_item in all_tasks:
        task_dict[get_task_coll(task_item)].append(task_item)
    return task_dict

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
