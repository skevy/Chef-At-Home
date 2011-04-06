import os

PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
LOCAL_DEV = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Adam Miskiewicz', 'adam.skevy@mac.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',                 # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'db', 'chefathome.db'), # Or path to database file if using sqlite3.
        'USER': '',                                             # Not used with sqlite3.
        'PASSWORD': '',                                         # Not used with sqlite3.
        'HOST': '',                                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                             # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
MEDIA_URL = '/media/'
MEDIA_URLS = ()

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static/')
STATIC_URL = '/static/'
STATIC_URLS = ()

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '5oobt_px9g877%&*#m7fgnq_(igh4!t&s&u%r^gn+g36%!x2id2bbivov'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'cah.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    
    'cah',
    'cah.meal_plans',
    'cah.menus',
    'cah.recipes',
        
    'django_extensions',
    'south',
    'social_auth',
    'taggit',
)

#Authentication

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY = 'yM3INdwrsRorYq5P1oGQQ'
TWITTER_CONSUMER_SECRET = 'lQHuDLGwLfI1X7T6qYpE9ULtoFuX33aKFvLaIn0GeqU'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'

FACEBOOK_APP_ID = '215301415149980'
FACEBOOK_API_SECRET = '3b1a8bcb808d4599642a67e18638aa8a'

from django.template.defaultfilters import slugify
SOCIAL_AUTH_USERNAME_FIXER = lambda u: slugify(u)
FACEBOOK_EXTENDED_PERMISSIONS=['email', ]

LOGIN_URL = '/account/auth/login/facebook/'
LOGIN_REDIRECT_URL = '/'

AUTH_PROFILE_MODULE = "cah.CAHProfile"

# CACHE_BACKEND = 'locmem://'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from j3utils.contrib.config import load_yaml
    load_yaml("/etc/chefathome/chefathome.yml", globals())
except:
    pass
    
try:
    from local_settings import *
except:
    pass