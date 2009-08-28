# -*- encoding: utf-8 -*-

import os.path

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'dashboard.views.dashboard'),
    (r'^staff/', include(admin.site.urls)),
    (r'^login/$', 'django_email_auth.views.login'),
    (r'^logout/', 'django_email_auth.views.logout'),
    (r'^dashboard/$', 'dashboard.views.dashboard'),
    (r'^profile/$', 'coaching.views.profile'),
    (r'^learning/', include('learning.urls')),
)

if settings.SITE_ID==1:
    # dev server
    contents_root = os.path.join(settings.PROJECT_PATH, settings.CONTENTS_PREFIX)
    urlpatterns += patterns('',
    (r'^static/contents/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': contents_root }),
)
