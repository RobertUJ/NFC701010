from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('nfc701010.apps.customers.views',
	url(r'^(?P<customer>[-\w]+)/(?P<zipcode>\d{1,6})/(?P<branch>[^\.]+)/$','get_customer',name='customer_view'),
	url(r'^(?P<customer>[-\w]+)/(?P<zipcode>\d{1,6})/$','get_all_branchs',name='get_all_branch_view'),
)