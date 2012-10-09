from django.contrib import admin
from django.contrib.admin import ModelAdmin
from nfc701010.apps.customers.models import ZipCode,Customer,Branch,PhotoGallery





class CustomerAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display        = ('name','slug',)
	search_fields		= ('name','slug',)

class PhotoGalleryAdmin(admin.ModelAdmin):
	pass

class PhotoGalleryInline(admin.StackedInline):
	model = PhotoGallery
	max_num = 50
	extra = 0

class BranchAdmin(admin.ModelAdmin):
	inlines = [PhotoGalleryInline,]
	prepopulated_fields = {"slug": ("name",)}
	list_display        = ('name','slug','Title',)
	search_fields		= ('name','slug','Title',)


admin.site.register(ZipCode)
# admin.site.register(PhotoGallery,PhotoGalleryAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Customer,CustomerAdmin)
