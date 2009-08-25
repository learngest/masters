# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^masters/', include('masters.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'dashboard.views.dashboard'),
    (r'^staff/', include(admin.site.urls)),
    (r'^login/', 'django_email_auth.views.login'),
    #(r'^logout/', 'django_email_auth.views.logout'),
    (r'^dashboard/', 'dashboard.views.dashboard'),
)
