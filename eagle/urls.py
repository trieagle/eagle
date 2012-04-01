from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'eagle.views.home', name='home'),
    # url(r'^eagle/', include('eagle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    


    ## for test
    url(r'^ajax/$', 'ajax.views.ajax'),
    url(r'^update/$', 'ajax.views.update'),
    url(r'^update2/$', 'ajax.views.update2'),
    url(r'^update3/$', 'ajax.views.update3'),

    url(r'^$', 'eagle.account.views.index'),
    url(r'^index/$','account.views.index'),
    url(r'^task/update/$', 'eagle.task.views.update_task'),
    url(r'^account/', include('eagle.account.urls')),
    url(r'^task/', include('eagle.task.urls')),
)

