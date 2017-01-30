from django.shortcuts import render
from . import Rider

def riders_list(request):
	riders = Rider.objects.all()
	return render(request, 'sledovani/riders_list.html', {})