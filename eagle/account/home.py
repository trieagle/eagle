#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from account.models import Account
from task import models as task_model
import collections;
import datetime
import calendar


COLL_TAG, COLL_DAY, COLL_WEEK, COLL_MONTH, COLL_OVER_MONTH, COLL_RECORD = range(6)

list_name = {COLL_TAG: "in tag",
             COLL_DAY: "on today",
             COLL_WEEK: "in this week",
             COLL_MONTH: "in this month",
             COLL_OVER_MONTH: "over a month",
             COLL_RECORD: "records"}

def get_task_coll(task_item):
    cur_date = datetime.datetime.now()
    if not task_item.alive:
        return COLL_RECORD 
    if task_item.done():
        return COLL_RECORD #not suitable!!! TODO
    if False and not task_item.active():
        return COLL_RECORD
        #not in use!!!'''
        #''' overdue tasks'''
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
        if cur_date.weekday() == 6: #the last day of the week, so the task must be done today
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
    task_dict = {COLL_TAG: [],
                 COLL_DAY: [],
                 COLL_WEEK: [],
                 COLL_MONTH: [],
                 COLL_OVER_MONTH: [],
                 COLL_RECORD: []}
    all_tasks = task_model.Task.objects.filter(owner=user_id)
    for task_item in all_tasks:
        task_dict[get_task_coll(task_item)].append(task_item)
    return task_dict

def home(request):
    '''xx_task contains tasks *must* to be done in xx'''
    account = Account.objects.get(user=request.user) 
    task_dict = fetch_lists(account.id)
    for _, li in task_dict.items():
        li.sort(key=lambda t: t.create_time)
    
    print '-----------------------------'
    for key, value in task_dict.items():
        print key, value
    print '-----------------------------'
    
    ordered_tasks_list = collections.OrderedDict(sorted(task_dict.items(), key=lambda t: t[0]))
    return render_to_response("common/index.html",
                              {"tasks_list": ordered_tasks_list,
                               "list_name": list_name},
                              context_instance=RequestContext(request))
