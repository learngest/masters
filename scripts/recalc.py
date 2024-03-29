#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys

try:
    import masters.settings
except ImportError:
    curdir, filename = os.path.split(__file__)
    sys.path.append(os.path.abspath(os.path.join(curdir, os.pardir, os.pardir)))
    import masters.settings

from django.core.management import setup_environ
setup_environ(masters.settings)

from apps.coaching.models import Utilisateur, Resultat, GranuleValide, ModuleValide
from apps.testing.models import Granule
from apps.coaching.controllers import UserState

for utilisateur in Utilisateur.objects.all():
    for g in (59, 60, 61, 62):
        granule = Granule.objects.get(pk=g)
        try:
            gv = GranuleValide.objects.get(
                    utilisateur=utilisateur,
                    granule=granule)
        except GranuleValide.DoesNotExist:
            resultats = Resultat.objects.filter(
                    utilisateur=utilisateur,
                    granule=granule).order_by('-score')
            if resultats:
                best = resultats[0]
                if best.score >= granule.score_min:
                    try:
                        GranuleValide.objects.get(
                                utilisateur=utilisateur,
                                granule=granule)
                    except GranuleValide.DoesNotExist:
                        gv = GranuleValide(
                                utilisateur=utilisateur,
                                granule=granule,
                                date=best.date,
                                score=best.score)
                        gv.save()
                    mvalide = True
                    for gr in granule.module.granule_set.all():
                        if utilisateur.granulevalide_set.filter(granule=gr).count() == 0:
                            mvalide = False
                            break
                    if mvalide:
                        try:
                            ModuleValide.objects.get(
                                    utilisateur=utilisateur,
                                    module=granule.module)
                        except ModuleValide.DoesNotExist:
                            mv = ModuleValide(
                                    utilisateur=utilisateur,
                                    date=best.date,
                                    module=granule.module)
                            mv.save()

    us = UserState(utilisateur)
    us.recalcule_tout(sauver=True)


