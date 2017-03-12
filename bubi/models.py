# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Kategorie:
	jmeno = models.CharField(100)
	
	def __unicode__(self):
		return self.jmeno

class Produkt:
	nazev = models.CharField(100)
	popis = models.TextField()
	obrazek = models.ImageField(upload_to='img/produkty', blank=True, null=True)
	cena = models.IntegerField()
	kategorie = models.ForeignKey('bubi.Kategorie')
	
	def __unicode__(self):
		return self.jmeno