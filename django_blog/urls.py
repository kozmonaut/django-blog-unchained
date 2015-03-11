from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Create urls for blog
    url(r'', include('blog.urls')),

    # Commenting engine
    # url(r'^comments/', include('django_comments.urls')),

    # URLS for Flat Pages
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # CKeditor inside post editor
    url(r'^ckeditor/', include('ckeditor.urls')),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
