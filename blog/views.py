from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render_to_response, render
from django.core.paginator import Paginator, EmptyPage
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

from blog.models import Category, Post, Tags

class CategoryView(ListView):
  def get_queryset(self):
		slug = self.kwargs['slug'] # Get slug from request
		try:
			category = Category.objects.get(slug=slug) 
			return Post.objects.filter(category=category) # Filter posts by fetched category name
		except Category.DoesNotExist: # If category not exist return empty post list
			return Post.objects.none() 

class TagsView(ListView):
	def get_queryset(self):
		slug = self.kwargs['slug']
		try:
			tag = Tags.objects.get(slug=slug)
			return tag.post_set.all()
		except Tags.DoesNotExist:
			return Post.objects.none()

def categoryList(request, page=0, paginate_by=5,
                  template_name='templates/blog/category_list.html',
                  extra_context=None,
                  **kwargs):

    return list_detail.object_list(
        request,
        queryset=Category.objects.all(),
        paginate_by=paginate_by,
        page=page,
        template_name=template_name,
        extra_context=extra_context,
        **kwargs
    )

def tagsList(request, page=0, paginate_by=5,
                  template_name='templates/blog/tags_list.html',
                  extra_context=None,
                  **kwargs):

    return list_detail.object_list(
        request,
        queryset=Tags.objects.all(),
        paginate_by=paginate_by,
        page=page,
        template_name=template_name,
        extra_context=extra_context,
        **kwargs
    )

def getSearchResults(request):
  
    # Get the query data
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    # Query the database
    results = Post.objects.filter(Q(desc__icontains=query) | Q(title__icontains=query))

    # Add pagination
    pages = Paginator(results, 5)

    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display the search results
    return render_to_response('blog/search_list.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': results})

def commentPosted(request):
    return HttpResponseRedirect('/')