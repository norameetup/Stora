from django.template import Context, loader
from django.http import HttpResponse
from rooms.models import Room, Member

def getAllRooms():
    rooms = Room.objects.all()
    
    return rooms

def index(request):
    t = loader.get_template('index/index.html')
    c = Context({'availableRooms': getAllRooms() })

    return HttpResponse(t.render(c))

