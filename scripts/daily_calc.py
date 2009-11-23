#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath('%s/../..' % __file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'masters.settings'
from django.conf import settings

dummy = settings.INSTALLED_APPS

from coaching.models import Utilisateur
from coaching.controllers import UserState

for utilisateur in Utilisateur.objects.all():
    us = UserState(utilisateur)
#    us.nb_cours_valides(recalcul=True,sauve=False)
#    us.nb_cours_en_retard(recalcul=True,sauve=False)
#    us.nb_cours_valides_en_retard(recalcul=True,sauve=False)
#    us.nb_travaux_rendus(recalcul=True,sauve=False)
#    us.cours_courant(recalcul=True,sauve=False)
#    us.nb_modules_in_current(recalcul=True,sauve=False)
#    us.nb_modules_valides_in_current(recalcul=True,sauve=False)
#    utilisateur.save()
    us.recalcule_tout(sauver=True)


