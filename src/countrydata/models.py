from __future__ import unicode_literals

from django.db import models

# Create your models here.

class country(models.Model):
	country_name = models.CharField(max_length=50)

	class Meta:
		verbose_name = "countrydata"
		verbose_name_plural = "countrydatas"

	def __str__(self):
		return "%s" % (self.country_name)

class state(models.Model):
	state_name 	= models.CharField(max_length=50)
	country 	= models.ForeignKey(country, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "state"
		verbose_name_plural = "states"

	def __str__(self):
		return "%s" % (self.state_name)

class city(models.Model):
	city_name	= models.CharField(max_length=50)
	country		= models.ForeignKey(country, on_delete=models.CASCADE)
	state 		= models.ForeignKey(state, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "city"
		verbose_name_plural = "citys"

	def __str__(self):
		return "%s" % (self.city_name)