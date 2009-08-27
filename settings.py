# -*- encoding: utf-8 -*-

import sys
import os.path
from django.utils.translation import ugettext_lazy as _

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

if LOCAL_APPS_PATH:
    sys.path.append(LOCAL_APPS_PATH)

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Sessions
SESSION_EXPIRE_AT_BROWSER_CLOSE = True                                                                            
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'uploads'),

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/uploads/'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/dashboard/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/media/'
# never put a beginning / on contents prefix
CONTENTS_PREFIX = 'static/contents'
ALLOWED_INCLUDE_ROOTS = (os.path.join(PROJECT_PATH, CONTENTS_PREFIX),)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%^)v@no(0iz_m5sx*mn#k2%#emm3m0117f2k4ltd+gg=ugz3ws'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_email_auth.middleware.EmailAuthMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'masters.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django_email_auth',
    'dashboard',
    'learning',
    'coaching',
)

AUTHENTICATION_BACKENDS = (
    'django_email_auth.backends.EmailBackend',
)

CUSTOM_USER_MODEL = 'coaching.Utilisateur'

LISTE_LANGUES = (
        ('fr', _('French')),
        ('en', _('English')),
        ('zh-cn', _('Simplified Chinese')),
)

LISTE_TYPES = (
        ('htm', 'HTML'),
        ('swf', 'Flash movie'),
        ('pdf', 'Portable Document Format'),
        ('doc', 'MS Word document'),
        ('xls', 'MS Excel document'),
)

