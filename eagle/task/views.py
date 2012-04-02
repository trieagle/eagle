#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from eagle.task.models import Task, Status


_minetype = 'application/javascript, charset=utf8'

def create_task(request):
    pass

def update_task(request):
    print 'in update'
    if request.is_ajax():
        taskObj = simplejson.loads(request.raw_post_data)
        print taskObj
        task = Task.objects.get(id=taskObj['id'])
        print task
        if task:
            task.title = taskObj['title']
            task.detail = taskObj['detail']
            task.save()
            new_task = Task.objects.filter(id=taskObj['id'])
            print new_task
            data = serializers.serialize('json',
                                         new_task)
            print data
            return HttpResponse(data, _minetype)
    return HttpResponse('error:not ajax request')

##only set task.alive = false
def remove_task(request):
    if request.is_ajax():
        taskObj = simplejson.loads(request.raw_post_data)
        task = Task.objects.get(id=taskObj['id'])
        if task:
            task.alive = False
            task.save()
            return HttpResponse(simplejson.dumps(True), _minetype)

    return HttpResponse('error:not ajax request')

def done_task(request):
    if request.is_ajax():
        req = simplejson.loads(request.raw_post_data)
        task_id = req['task_id']
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
        if status:
            status.delete()
            data = serializers.serialize('json',[status]) ##only serialize queryset
            return HttpResponse(data, _minetype)

    return HttpResponse('error:not ajax request')
