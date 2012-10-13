from django.contrib.admin import *
from django.contrib import admin
from nfc701010.apps.customers.models import ZipCode,Customer,Branch,PhotoGallery
from sorl.thumbnail.admin import AdminImageMixin


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
	list_display        = ('name','Title','urltobranch',)
	list_filter         = ('ZipCode__zipcode','Customer__name',)
	search_fields		= ('name','slug','Title','ZipCode__zipcode','Customer__name',)
	
	def urltobranch(self,instance):
		_url = '/%s/%s/%s/' % (instance.Customer.slug,instance.ZipCode.zipcode,instance.slug)
		return 	'<a target="_blank" href="%s">%s</a>' % (_url,_url)
	urltobranch.short_description = 'Url Shortcut'
	urltobranch.allow_tags = True

admin.site.register(ZipCode)
# admin.site.register(PhotoGallery,PhotoGalleryAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Customer,CustomerAdmin)
