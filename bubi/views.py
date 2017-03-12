# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from .models import Kategorie, Produkt

def home(request):
	return kategorie(request, 'burgery')

def kategorie(request, kat):
	katloc = {
		'burgery': u'Burgery',
		'special': u'Speciální burgery',
		'kalamary': u'Kalamáry',
		'prilohy': u'Přílohy',
		'napoje': u'Nápoje',
	}
	
	if kat not in ['burgery', 'special', 'kalamary', 'prilohy', 'napoje']:
		prods = Produkt.objects.get()
	else:
		prods = Produkt.objects.filter(kategorie__jmeno=kat).order_by('nazev').distinct()
	return render(request, 'bubi/category.html', {'produkty': prods})

def produkt(request, pk):
	produkt = get_object_or_404(Produkt.objects.get(pk=pk))
	return render(request, 'bubi/detail.html', {'produkt': produkt})