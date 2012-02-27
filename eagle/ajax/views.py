#Create your views here.
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse

def ajax(request):
    return render_to_response('ajax.html', {})

def update(request):
    sample = {'name':'skyshaw', 'major':'cs'}
    print sample
    return HttpResponse(
        simplejson.dumps(sample),
        content_type='application/javascript; charset=utf8')
