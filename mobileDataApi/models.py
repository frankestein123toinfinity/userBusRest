# Create your models here.

from django.db import models

class BusDatalist(models.Model):
	id = models.IntegerField(primary_key=True, blank=False, unique=True)
	busStopId = models.IntegerField(blank=False, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.id, self.busStopId)