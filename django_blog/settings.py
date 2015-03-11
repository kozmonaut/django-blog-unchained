""" Django settings for django_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6(bg@u&97mtybf2^p#z+cvdy3h6ok=0k_cdxb^03&eel08d_w2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Needed for flatpages
SITE_ID = 1

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'blog', 
    'django.contrib.sites',
    'django.contrib.flatpages',
    #'django_comments',
    'ckeditor',
    'disqus'
)

# Disqus 
DISQUS_API_KEY = 'FOOBARFOOBARFOOBARFOOBARFOOBARF'
DISQUS_WEBSITE_SHORTNAME = 'foobar'

# Template directory
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

PROJECT_APPS = ['blog']

# Paths for storing media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = "uploads/"

# Ckeditor plugin
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# Ckeditor plugins
CKEDITOR_CONFIGS = {
'default': {
    'toolbar': 'CMS',
    'toolbar_CMS': [
        {
            'name': 'basicstyles',
            'groups': ['basicstyles', 'cleanup'],
            'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']
        },
        {
            'name': 'paragraph',
            'groups': ['list', 'indent', 'blocks'],
            'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']
        },
        {
            'name': 'links',
            'items': ['Link', 'Unlink']
        },
        {
            'name': 'insert',
            'items': ['Image', 'HorizontalRule', 'Table', 'Iframe', ]
        },
        {
            'name': 'colors',
            'items': ['TextColor', 'BGColor']
        },

        { 
            'name': 'styles', 
            'items' : [ 'Styles','Format','Font','FontSize' ]
        },

        {
            'name': 'document', 
            'items' : [ 'Source','-','Save','NewPage','DocProps','Preview','Print','-','Templates' ] 
        },

        {
            'name': 'youtube',
            'items': ['youtube',]
        },
    ],
},
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', # For flatpages
)

ROOT_URLCONF = 'django_blog.urls'

WSGI_APPLICATION = 'django_blog.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Heroku config
# Parse database configuration from $DATABASE_URL

#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Static asset configuration
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog/static'),
)

# Memcached config
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
