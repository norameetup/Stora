from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	owner = models.CharField(max_length=200)
	ctime = models.DateTimeField('date created')

	def __unicode__(self):
		return self.name
