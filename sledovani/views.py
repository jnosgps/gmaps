from django.shortcuts import render
from .models import Rider

def riders_list(request):
	riders = Rider.objects.all().order_by('up')
	return render(request, 'sledovani/riders_list.html', {
		'riders': riders,
	})