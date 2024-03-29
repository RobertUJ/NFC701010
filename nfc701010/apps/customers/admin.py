from django.contrib.admin import *
from django.contrib import admin
from nfc701010.apps.customers.models import ZipCode,Customer,Branch,PhotoGallery,phone_info
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.admin.filters import AllValuesFieldListFilter


class CustomerAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display        = ('name','slug',)
	search_fields		= ('name','slug',)

class PhotoGalleryAdmin(AdminImageMixin, admin.ModelAdmin):
	pass

class PhotoGalleryInline(AdminImageMixin, admin.StackedInline):
	model = PhotoGallery
	verbose_name = "Photo"
	max_num = 50
	extra = 0

class BranchAdmin(AdminImageMixin, admin.ModelAdmin):
	inlines = [PhotoGalleryInline,]
	prepopulated_fields = {"slug": ("name",)}
	list_display        = ('customer_name', 'name','Title','urltobranch','tag_id')
	list_filter         = ('ZipCode__zipcode','Customer__name','tag_id','featured',)
	search_fields		= ('name','tag_id','slug','Title','ZipCode__zipcode','Customer__name',)
	
	def customer_name(self,instance):
		return '%s' %(instance.Customer.name)
	customer_name.short_description = "Customer Name"



	def urltobranch(self,instance):
		_url = '/%s/%s/%s/' % (instance.Customer.slug,instance.ZipCode.zipcode,instance.slug)
		return 	'<a target="_blank" href="%s">%s</a>' % (_url,_url)
	urltobranch.short_description = 'Url Shortcut'
	urltobranch.allow_tags = True

class phone_infoAdmin(admin.ModelAdmin):
	list_display        = ('zipcode','area','mobile',)
	search_fields		= ('zipcode','area','mobile',)
	list_filter         = ('zipcode','area','branch__Title')



admin.site.register(ZipCode)
# admin.site.register(PhotoGallery,PhotoGalleryAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(phone_info,phone_infoAdmin)
