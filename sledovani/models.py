from django.db import models
from django.utils import timezone

class Rider(models.Model):
	name = models.CharField(max_length=32)
	delka = models.CharField(max_length=10)
	sirka = models.CharField(max_length=10)
	up = models.DateTimeField(default=timezone.now)
	
	def update(self, dx, dy):
		delka = dx
		sirka = dy
		up = timezone.now()
		self.save()
	
	def __str__(self):
		return self.name