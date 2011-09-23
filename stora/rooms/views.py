from django.template import Context, loader
from django.http import HttpResponse
from rooms.models import Room
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import time
from datetime import date


def getRoomInfo( room_id ):
	room = Room.objects.get(id=room_id)
	return room;


def index(request, room_id):
	
	room = getRoomInfo( room_id )
	if request.method == "POST":
		dateF = request.POST['date']
		durationF = request.POST['duration']
		sizeF = request.POST['size']
		
		room.reservation_set.create(res_time=date.today(), duration=durationF, size=sizeF)
		
	
	
	return render_to_response('rooms/index.html', {'room': getRoomInfo( room_id )},
							   context_instance=RequestContext(request))



