#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import datetime

try:
    import masters.settings
except ImportError:
    curdir, filename = os.path.split(__file__)
    sys.path.append(os.path.abspath(os.path.join(curdir, os.pardir, os.pardir)))
    import masters.settings

from django.core.management import setup_environ
setup_environ(masters.settings)

from apps.coaching.models import Utilisateur, Event
from apps.coaching.controllers import UserState

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

date_limite = datetime.datetime.now() - datetime.timedelta(7)
for event in  Event.objects.filter(date__lt=date_limite):
    event.delete()

