from django.shortcuts import render, get_object_or_404
from .models import Rider
from .forms import DestinationForm

def riders_list(request):
	riders = Rider.objects.all().order_by('up')
	return render(request, 'sledovani/riders_list.html', {
		'riders': riders,
	})

def rider_detail(request, pk):
	rider = get_object_or_404(Rider, pk=pk)
	
	return render(request, 'sledovani/rider_detail.html', {
		'rider': rider,
	})