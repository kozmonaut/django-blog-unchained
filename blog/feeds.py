from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from blog.models import Post

class Feeds(Feed):
	title = 'dropSQL feeds'
	description = 'Post feeds'

	def link(self):
		return reverse('categoryList')

	def items(self):
		return Post.objects.all()[:5]

	def item_title(self, obj):
		return obj.title

	def item_description(self, obj):
		return obj.desc

	def item_pubdate(self,obj):
		return obj.pub_date