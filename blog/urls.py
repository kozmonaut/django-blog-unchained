from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.views import CategoryView, TagsView
from feeds import Feeds
from blog.models import Post, Category, Tags

urlpatterns = patterns('',

	# Implement pagination
	url(r'^(?P<page>\d+)?/?$', ListView.as_view(
		model = Post,
		paginate_by = 5,
		)),
	
	# Posts
	url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        )),

    # Categories
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryView.as_view(
        paginate_by=8,
        model=Category,
        )),

    # Tags
    url(r'^tag/(?P<slug>[a-zA-Z0-9]+)/?$', TagsView.as_view(
    	paginate_by=8,
    	model=Tags,
    	)),

    # Comment redirect
    # url(r'^comments/posted/$', 'blog.views.commentPosted' ),

    # List categories
    url(r'^category/$', 'blog.views.categoryList', name='categoryList'),

    # List tags 
    url(r'^tag/$', 'blog.views.tagsList', name='tagsList'),

    # Search
    url(r'^search/$', 'blog.views.getSearchResults'),

    # Fetch RSS feeds
    url(r'^rss/$', Feeds()),
) 

# Index page (match only an empty string)
'''url('^$', ListView.as_view(model=Post,)),'''