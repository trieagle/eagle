from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^medias/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),                       
)

urlpatterns += patterns('',
    url(r'^$', 'accounts.views.index',name="index"),
    url(r'^main$', 'checker.views.main',name="main"),
)

urlpatterns += patterns('',
    url(r'^accounts/index$', 'accounts.views.index',name="accounts_index"),
    url(r'^accounts/register$', 'accounts.views.register',name="register"),
    url(r'^accounts/login$', 'accounts.views.login',name="login"),
    url(r'^accounts/logout$', 'accounts.views.logout',name="logout"),                         
)

urlpatterns += patterns('',
    url(r'^routine/(?P<r_id>\d+)/$', 'checker.views_routine.show_routine',name="show_routine"),
    url(r'^routine/(?P<r_id>\d+)/done/$', 'checker.views_routine.done_routine',name="done_routine"),
    url(r'^routine/(?P<r_id>\d+)/undone/$', 'checker.views_routine.undone_routine',name="undone_routine"), 
    url(r'^routine/(?P<r_id>\d+)/remove/$', 'checker.views_routine.remove_routine',name="remove_routine"), 
    url(r'^add_routine$', 'checker.views_routine.add_routine',name="add_routine"),
)

urlpatterns += patterns('',
    url(r'^casething/(?P<c_id>\d+)/$', 'checker.views_casething.show_casething',name="show_casething"),
    url(r'^casething/(?P<c_id>\d+)/remove/$', 'checker.views_casething.remove_casething',name="remove_casething"), 
    url(r'^add_casething$', 'checker.views_casething.add_casething',name="add_casething"),
)
        
