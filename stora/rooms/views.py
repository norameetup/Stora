from django.template import Context, loader
from django.http import HttpResponse
from rooms.models import Room


def getRoomInfo( room_id ):
	room = Room.objects.get(id=room_id)
	return room;


def index(request, room_id):
	t = loader.get_template('rooms/index.html')
	c = Context({'room': room_id,})

	return HttpResponse(t.render(c))


