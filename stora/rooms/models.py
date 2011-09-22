from django.db import models

class Member(models.Model):
	name = models.CharField(max_length=200)
	points = models.IntegerField()
	
	def __unicdoe__(self):
		return self.name

class Room(models.Model):
	member = models.ForeignKey(Member)
	name = models.CharField(max_length=200)
	description = models.TextField()
	size = models.IntegerField()
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=20)
	zip = models.IntegerField()
	ctime = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.name
