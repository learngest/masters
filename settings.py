# -*- encoding: utf-8 -*-

import sys
import os.path

try:
    from local_settings import *
except ImportError:
    pass

try:
    from dev_settings import *
except ImportError:
    pass

try:
    from prod_settings import *
except ImportError:
    pass

try:
    if LG_LOCAL_APPS_PATH:
        sys.path.append(LG_LOCAL_APPS_PATH)
except NameError:
    pass

LG_PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'
DATETIME_FORMAT = "Y-m-d H:i:s"
DATE_FORMAT = 'd M Y'
DATETIME_INPUT_FORMATS = ('%d/%m/%Y %H:%M:%S', '%d-%m-%Y %H:%M:%S',
                          '%d/%m/%Y', '%d-%m-%Y',)
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y',)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Sessions
SESSION_EXPIRE_AT_BROWSER_CLOSE = True                                                                            
ROOT_URLCONF = 'masters.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/dashboard/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/media/admin/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'apps.coaching.context_processors.media_urls',
        'django.core.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'email_auth.middleware.EmailAuthMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(LG_PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'email_auth',
    'apps.dashboard',
    'apps.learning',
    'apps.coaching',
    'apps.testing',
)

AUTHENTICATION_BACKENDS = (
#    'email_auth.backends.EmailBackend',
    'apps.coaching.backends.Backend',
)

CUSTOM_USER_MODEL = 'coaching.Utilisateur'

