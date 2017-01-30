from django.db import models
from django.utils import timezone

class Rider(models.Model):
	name = models.CharField(max_length=32)
	delka = models.CharField(max_length=18)
	sirka = models.CharField(max_length=18)
	up = models.DateTimeField(auto_now=True)
	
	def update(self, dx, dy):
		delka = dx
		sirka = dy
		up = timezone.now()
		self.save()
		print delka, sirka
	
	def __str__(self):
		return self.name