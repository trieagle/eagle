#coding=utf-8

from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

import datetime

## combine add and update operation
def update_task(request):
	if request.is_ajax():
        req = simplejson.loads(request.raw_post_data)
        task = Task.objects.get(id=req['task_id'])
		
		if task
			## tobe completed
			data = serializers.serialize('json',[task]) ##only serialize queryset
        	minetype = "application/javascript, charset=utf8"
        	return HttpResponse(data,minetype)
    
    return HttpResponse('error:not ajax request')

##only set task.alive = false
def remove_task(request):
    if request.is_ajax():
        req = simplejson.loads(request.raw_post_data)
        task = Task.objects.get(id=req['task_id'])
		if task
			task.alive = false
			task.save()
			data = serializers.serialize('json',[task]) ##only serialize queryset
        	minetype = "application/javascript, charset=utf8"
        	return HttpResponse(data,minetype)
    
    return HttpResponse('error:not ajax request')

def done_task(request):
    if request.is_ajax():
        req = simplejson.loads(request.raw_post_data)
        task_id=req['task_id']
		_rate = req['rate']
        _task = Task.objects.get(id=task_id)
		status = Status.objects.create(task=_task,rate=_rate)
		status.save()
		data = serializers.serialize('json',[status]) ##only serialize queryset
        minetype = "application/javascript, charset=utf8"
        return HttpResponse(data,minetype)
    
    return HttpResponse('error:not ajax request')

def undone_task(request):
   if request.is_ajax():
        req = simplejson.loads(request.raw_post_data)
        _task = Task.objects.get(id=req['task_id'])
		status = Status.objects.filter(task=_task,rate=_rate).latest("date")
		if status		
			status.delete()
			data = serializers.serialize('json',[status]) ##only serialize queryset
        	minetype = "application/javascript, charset=utf8"
       		return HttpResponse(data,minetype)
    
    return HttpResponse('error:not ajax request')
        
    
