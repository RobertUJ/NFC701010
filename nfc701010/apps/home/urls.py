from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('nfc701010.apps.home.views',
	url(r'^$','index_view',name='main_view'),
	url(r'^contact/$','contact_view',name='contact_view'),
)