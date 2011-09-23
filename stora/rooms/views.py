from django.template import Context, loader
from django.http import HttpResponse
from rooms.models import Room, Reservation
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import time, datetime


def getRoomInfo( room_id ):
	room = Room.objects.get(id=room_id)
	return room;


def index(request, room_id):
	
	room = getRoomInfo( room_id )
	currentReservations = Reservation.objects.filter(room = room.id)
	status = ""
	
	if request.method == "POST":
		dateF = request.POST['date']
		durationF = request.POST['duration']
		sizeF = '10'
		
		time_format = "%m/%d/%Y %H:%M"
		dMan = datetime.datetime.fromtimestamp(time.mktime(time.strptime(dateF, time_format)))
		
		for res in currentReservations:
			if res.res_time == dMan:
				status = "taken"
				break;

		if status != "taken":
			room.reservation_set.create(res_time=dMan, duration=durationF, size=sizeF)
			status = "posted"
		
		
	
	
	return render_to_response('rooms/index.html', {'room': room, 'reservations':currentReservations, 'status': status},
							   context_instance=RequestContext(request))



