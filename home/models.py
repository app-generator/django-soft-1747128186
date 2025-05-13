# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    vorname = models.CharField(max_length=255, null=True, blank=True)
    nachname = models.CharField(max_length=255, null=True, blank=True)
    beruf = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Artikel(models.Model):

    #__Artikel_FIELDS__
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    gekauft = models.DateTimeField(blank=True, null=True, default=timezone.now)
    anzahl = models.IntegerField(null=True, blank=True)

    #__Artikel_FIELDS__END

    class Meta:
        verbose_name        = _("Artikel")
        verbose_name_plural = _("Artikel")


class Leihliste(models.Model):

    #__Leihliste_FIELDS__
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    ausgeliehen_von = models.ForeignKey(Lehrlinge, on_delete=models.CASCADE)
    ausleihdatum = models.DateTimeField(blank=True, null=True, default=timezone.now)
    rückgabedatum = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Leihliste_FIELDS__END

    class Meta:
        verbose_name        = _("Leihliste")
        verbose_name_plural = _("Leihliste")


class Lehrlinge(models.Model):

    #__Lehrlinge_FIELDS__
    vorname = models.CharField(max_length=255, null=True, blank=True)
    nachname = models.CharField(max_length=255, null=True, blank=True)
    geburstag = models.DateTimeField(blank=True, null=True, default=timezone.now)
    beruf = models.TextField(max_length=255, null=True, blank=True)

    #__Lehrlinge_FIELDS__END

    class Meta:
        verbose_name        = _("Lehrlinge")
        verbose_name_plural = _("Lehrlinge")



#__MODELS__END
