from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('account.views',
    url(r'index/$', 'index'),
    url(r'register/$', 'register'),
    url(r'login/$', 'login'),
    url(r'logout/$', 'logout'),
    url(r'userinfo/$', 'userinfo'),  
)
