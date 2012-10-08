from django.db import models
from django.template.defaultfilters import slugify
#from sorl.thumbnail import ImageField


class CodeZip(models.Model):
	ZIP 		= models.PositiveIntegerField(null=False,blank=False,unique=True)
	def __unicode__(self):
		return str(self.ZIP)


class Customer(models.Model):
	zipcode 	=  models.ForeignKey(CodeZip)
	name 		=  models.CharField(max_length=255,null=False,blank=False,unique=True,verbose_name=u'Client Name')
	slug		=  models.SlugField(max_length=255,null=True,blank=True,unique=True)
	def __unicode__(self):
		return str(self.name)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Customer,self).save(*args,**kwargs)

class Branch(models.Model):
	zipcode 	= models.ForeignKey(CodeZip)
	name 		= models.CharField(max_length=255,null=False,blank=False,unique=True)
	slug 		= models.SlugField(max_length=255,null=True,blank=True,unique=True)
	def __unicode__(self):
		return str(self.name)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Branch,self).save(*args,**kwargs)

class Info_branch(models.Model):
	branch 			= models.ForeignKey(Branch, unique=True,null=False,blank=False)
	Title 			= models.CharField(max_length=255)
	Logo  			= models.ImageField(upload_to='branch/logos')
	Video			= models.TextField(help_text='After making your selection in youtube, copy and paste the embed code of the video selected.')
	Coupon			= models.ImageField(upload_to='branch/cupon')
	Description		= models.TextField()
	Contact			= models.TextField()
	facebook		= models.URLField(max_length=200,verify_exists=True,null=True,blank=True)
	gmail			= models.URLField(max_length=200,verify_exists=True,null=True,blank=True)
	twitter			= models.URLField(max_length=200,verify_exists=True,null=True,blank=True)
	mail 			= models.EmailField(max_length=255)
	def __unicode__(self):
		return str(self.Title)


class PhotoGallery(models.Model):
	branch 			= models.ForeignKey(Branch)
	Image_Title	    = models.CharField(max_length=255)
	Image 			= models.ImageField(upload_to='branch/galery')
	def __unicode__(self):
		return str(self.Image_Title)








