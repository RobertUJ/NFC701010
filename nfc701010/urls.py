from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nfc701010.views.home', name='home'),
    # url(r'^nfc701010/', include('nfc701010.foo.urls')),

    #import urls.py's apps
     url(r'^',include('nfc701010.apps.home.urls')),
     url(r'^',include('nfc701010.apps.customers.urls')),

     

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
)
