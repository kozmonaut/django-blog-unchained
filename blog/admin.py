from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

import blog.models
from ckeditor.widgets import CKEditorWidget

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	exclude = ('author',) # Exclude author name from post

	# Author is making HTTP request
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()
 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm

# Register models to admin interface
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(blog.models.Post, PostAdmin)
admin.site.register(blog.models.Tags)
admin.site.register(blog.models.Category)