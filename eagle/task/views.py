#coding=utf-8

from django.http import HttpResponse
from django.utils import simplejson

from eagle.task.models import Task, Status

def add_task(request):
	pass

def update_task(request):
	if request.is_ajax():
        req = simplejson.loads(request.raw_post_data)
        ##task = Task.objects.get_object_or_create(id=req['task_id'])
		task = Task.objects.get(id=req['task_id'])
		if task
			task.title = req['title']
			task.detail = req['detail']
			task.save()
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
        
    
