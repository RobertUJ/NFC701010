from django.contrib import admin
from django.contrib.admin import ModelAdmin
from nfc701010.apps.customers.models import CodeZip,Customer,Branch,Info_branch,PhotoGallery


admin.site.register(CodeZip)

class CustomerAdmin(admin.ModelAdmin):
	list_display        = ('name','slug')
	ordering            = ('name')
	search_fields		= ('name','slug')

admin.site.register(Customer)


admin.site.register(Branch)
admin.site.register(Info_branch)
admin.site.register(PhotoGallery)