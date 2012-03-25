from django.conf.urls.defaults import include
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'task.views',
    url(r'create/$', ''),
    url(r'taskinfo/$', ''),
    url(r'taskinfo/update/$', ''),
    url(r'taskinfo/delete/$', ''))
