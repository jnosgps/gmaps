from django.shortcuts import render, get_object_or_404
from .models import Rider

def riders_list(request):
	riders = Rider.objects.all().order_by('up')
	return render(request, 'sledovani/riders_list.html', {
		'riders': riders,
	})

def rider_detail(request, pk):
	rider = get_object_or_404(Rider, pk=pk)
	if request.method == 'POST':
		lat = request.POST.get('lat')
		lng = request.POST.get('lng')
		rider.update(lat, lng, lat, lng)
		#rider.delka = lat
		#rider.sirka = lng
		#rider.save()
		#print 'LAT:', request.POST.get('lat'), 'LNG:', request.POST.get('lng')
	
	return render(request, 'sledovani/rider_detail.html', {
		'rider': rider
	})