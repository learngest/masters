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

from django.template.loader import render_to_string
from django.utils.encoding import smart_str

from apps.coaching.models import Groupe
from apps.learning.models import ModuleCours

liste = []

for groupe in Groupe.objects.order_by('client','nom',):
    groupe.nb_cours = groupe.cours.count()
    groupe.nb_modules = 0
    for c in groupe.cours.all():
        groupe.nb_modules += ModuleCours.objects.filter(cours=c).count()
    groupe.nb_logins = groupe.utilisateur_set.count()
    auj = datetime.date.today()
    hier = auj - datetime.timedelta(1)
    groupe.hier = groupe.utilisateur_set.filter(
            last_login__gte=hier,last_login__lt=auj).count()
    if groupe.hier:
        if len(groupe.client.nom) > 19:
            groupe.clientname = groupe.client.nom[:15]+"..."
        else:
            groupe.clientname = groupe.client.nom
        if len(groupe.nom) > 19:
            groupe.nom = groupe.nom[:15]+"..."
        liste.append(groupe)

report = render_to_string('report.txt', {'liste_groupes': liste, 'hier': hier,})
print smart_str(report)
