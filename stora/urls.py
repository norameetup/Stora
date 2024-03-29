from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^rooms/(?P<room_id>\d+)/$', 'rooms.views.index'),
	(r'^rooms/(?P<room_id>\d+)/api/(?P<date>.+)/$', 'rooms.views.api'),
	(r'^$', 'index.views.index'),
	(r'^api/$', 'index.views.api'),
  url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/usr/local/stora_fun/static'}),

  # Examples:
    # url(r'^$', 'stora.views.home', name='home'),
    # url(r'^stora/', include('stora.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
