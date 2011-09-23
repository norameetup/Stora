from django.db import models
from django import forms

class Room(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	icon = models.TextField(max_length=200)
	price = models.IntegerField()
	capacity = models.IntegerField()
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=20)
	zip = models.IntegerField()
	lat = models.FloatField()
	lon = models.FloatField()
	ctime = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.name
	
class Reservation(models.Model):
	room = models.ForeignKey(Room)
	res_time = models.DateTimeField()
	duration = models.IntegerField()
	size = models.IntegerField()
	
	def __unicode__(self):
		return self.room + " for " + self.res_time 


class SearchForm(forms.Form):
    zipcode = forms.IntegerField()
    date = forms.DateField()
    capacity = forms.IntegerField();
