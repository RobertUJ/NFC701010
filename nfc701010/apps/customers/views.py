from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives # Para enviar HTML
from django.http import HttpResponseRedirect
from django.http import Http404

from nfc701010.apps.customers.models import CodeZip,Customer,Branch,Info_branch,PhotoGallery 



def get_customer(request,customer,zipcode,branch):
	slug_customer = str(customer)
	zipcode  = int(zipcode)
	slug_branch   = str(branch)
	
	mZipCode = get_object_or_404(CodeZip,ZIP=zipcode)

	mcustomer = get_object_or_404(Customer,slug=slug_customer)
	if mcustomer.zipcode != mZipCode:
		raise Http404

	mBranch = get_object_or_404(Branch,slug=slug_branch)
	Info_Branch = get_object_or_404(Info_branch,branch=mBranch)
	# Get customer
	# mCustomer = get_object_or_404(Customer,slug=slug_customer)
	# CustomerZipCode = mCustomer.zipcode.ZIP 
	# if CustomerZipCode != zipcode:
	# 	raise Http404
	# else:
	# 	mBranch = get_object_or_404(Branch,slug=slug_branch)
	# mInfoBranch = get_object_or_404(Info_branch,branch=mBranch)
	try:
		mGalery = PhotoGallery.objects.filter(branch=mBranch)
	except PhotoGallery.DoesNotExist:
		mGalery = None
	ctx = {'infobranch':Info_Branch,'galery':mGalery}
	return render_to_response('customers/customer.html',ctx,context_instance=RequestContext(request))




	





