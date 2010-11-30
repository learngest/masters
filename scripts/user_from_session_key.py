#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import optparse

sys.path.append(os.path.dirname(os.path.abspath('%s/../..' % __file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'masters.settings'
from django.conf import settings

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

dummy = settings.INSTALLED_APPS

def user_from_session_key(sessionid):
    try:
        session = Session.objects.get(session_key=sessionid)
    except Session.DoesNotExist:
        return "Session %s does not exist" % sessionid
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)

    return user.id, user.username, user.email 


if __name__ == "__main__":

    p = optparse.OptionParser(
        description='Get user from session key in error mails',
        prog='get_user_from_session_key',
        version='0.01',
        usage='usage: %prog session_key',)
    options, arguments = p.parse_args()

    if len(arguments) != 1:
        p.print_help()
        sys.exit()

    print user_from_session_key(arguments[0])
    
