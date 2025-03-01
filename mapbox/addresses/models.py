import geocoder

from django.db import models


# Create your models here.

mapbox_access_token = 'pk.eyJ1IjoiZGFtYW5rYW1ib2oiLCJhIjoiY2tvMWJvY3NtMDZ6YTJvbzNzYnByZTQydSJ9.LL4CzpAhDnyqzAu6NX-65Q'

class Address(models.Model):
	address = models.TextField()
	lat = models.FloatField(blank=True,null=True)
	lang = models.FloatField(blank=True,null=True)

	def save(self,*args,**kargs):
		g = geocoder.mapbox(self.address,key=mapbox_access_token)
		g = g.latlng 
		self.lat = g[0]
		self.lang = g[1]
		return super(Address,self).save(*args,**kargs)
