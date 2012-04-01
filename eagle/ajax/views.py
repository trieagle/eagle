#Create your views here.
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext
from django.contrib.auth.models import User


def ajax(request):
    return render_to_response('ajax/ajax.html',
                              {},
                              context_instance=RequestContext(request))

def update(request):
    sample = {'name':'skyshaw', 'major':'cs'}
    jsample = simplejson.dumps(sample);
    print type(jsample)
    return HttpResponse(
        jsample,
        content_type='application/javascript; charset=utf8')

def update2(request):
    if request.is_ajax():
        req = simplejson.loads(request.raw_post_data)
        uname=req['username']
        user = User.objects.filter(username=uname) ##result is queryset
        data = serializers.serialize('json', user) ##only serialize queryset
        minetype = "application/javascript, charset=utf8"
        return HttpResponse(data,minetype)
    
    return HttpResponse('error:not ajax request')
