from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eagle.views.home', name='home'),
    # url(r'^eagle/', include('eagle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ajax.views.ajax'),
    url(r'^ajax/$', 'ajax.views.ajax'),
    url(r'^update/$', 'ajax.views.update'),
    url(r'^update2/$', 'ajax.views.update2'),
    url(r'^update3/$', 'ajax.views.update3'),
)
