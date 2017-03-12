# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Kategorie(models.Model):
	jmeno = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.jmeno

class Produkt(models.Model):
	nazev = models.CharField(max_length=100)
	popis = models.TextField()
	obrazek = models.ImageField(upload_to='img/produkty', blank=True, null=True)
	cena = models.IntegerField()
	kategorie = models.ForeignKey('bubi.Kategorie')
	
	def __unicode__(self):
		return self.nazev