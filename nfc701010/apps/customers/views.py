from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives # Para enviar HTML
from django.http import HttpResponseRedirect
from django.http import Http404

from nfc701010.apps.customers.models import ZipCode,Customer,Branch,PhotoGallery 
from nfc701010.apps.customers.forms import formInfoPhone




def get_customer(request,customer,zipcode,branch):
	_slug_customer = str(customer)
	_zipcode  = int(zipcode)
	_slug_branch   = str(branch)
	
	mCustomer 	= 	get_object_or_404(Customer,slug=_slug_customer)
	mZipCode 	= 	get_object_or_404(ZipCode,zipcode=_zipcode)
	mBranch 	= 	get_object_or_404(Branch,Customer=mCustomer,ZipCode=mZipCode,slug=_slug_branch)

	try:
		mGalery = PhotoGallery.objects.filter(Branch=mBranch)
	except PhotoGallery.DoesNotExist:
		mGalery = None
	
	""" Formulario para la peticion de numero de telefono """

	if request.is_ajax():
		mformPhone = formInfoPhone(request.POST)
		if mformPhone.is_valid():
			mfrmPhoneUncommited = mformPhone.save(commit=False)
			mfrmPhoneUncommited.branch = mBranch
			mfrmPhoneUncommited.save()
			return "Save Phone"
	else:
		mformPhone = formInfoPhone()


	ctx = {'infobranch':mBranch,'galery':mGalery,'frmPhone':mformPhone}
	return render_to_response('customers/customer.html',ctx,context_instance=RequestContext(request))


def get_all_branchs(request,customer,zipcode):
	_slug_customer = str(customer)
	_zipcode  = int(zipcode)
	
	mZipCode 	= 	get_object_or_404(ZipCode,zipcode=_zipcode)
	mcustomer 	= 	get_object_or_404(Customer,slug=_slug_customer)
	mBranch 	= 	Branch.objects.filter(ZipCode=mZipCode,Customer=mcustomer).order_by('-id')

	ctx = {'branchs':mBranch}
	return render_to_response('customers/allbranchs.html',ctx,context_instance=RequestContext(request))
	

	




