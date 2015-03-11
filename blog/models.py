from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.text import slugify

from ckeditor.fields import RichTextField

# Class for post category
class Category(models.Model):
	name = models.CharField(max_length=150)
	text = models.TextField()
	slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

	def __unicode__(self):
		return self.name

	# Check if is slug set
	def save(self):
		if not self.slug:
			self.slug = slugify(unicode(self.name))
		super(Category, self).save()

	def get_absolute_url(self):
		return "/category/%s/" % (self.slug)

	class Meta:
		verbose_name_plural = 'categories'

# Class for post tags
class Tags(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

	def save(self):
		if not self.slug:
			self.slug = slugify(unicode(self.name))
		super(Tags, self).save()

	def get_absolute_url(self):
		return "/tag/%s/" % (self.slug)

	def __unicode__(self):
		return self.name

# Create class for Post
class Post(models.Model):
	# Define attributes
	title = models.CharField(max_length=150)
	pub_date = models.DateTimeField()
	desc = RichTextField()
	slug = models.SlugField(max_length=50, unique=True)
	authors = models.ForeignKey(User)
	category = models.ForeignKey(Category,blank=True, null=True)
	tags = models.ManyToManyField(Tags)

	# Define URL structure
	def get_absolute_url(self):
		return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

	def __unicode__(self):
		return self.title

	class Meta:
		# Order posts by date
		ordering = ["-pub_date"]

