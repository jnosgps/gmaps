from django.db import models
from django.utils import timezone

class Rider(models.Model):
	name = models.CharField(max_length=32)
	delka = models.CharField(max_length=18)
	sirka = models.CharField(max_length=18)
	up = models.DateTimeField(auto_now=True)
	lat = models.DecimalField(max_digits=10, decimal_places=6)
	lng = models.DecimalField(max_digits=10, decimal_places=6)
	
	def update(self, dx, dy, lat, lng):
		self.delka = dx
		self.sirka = dy
		self.lat = lat
		self.lng = lng
		up = timezone.now()
		self.save()
	
	def __str__(self):
		return self.name