from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from rooms.models import Room, Reservation
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.utils import simplejson
import random
from django.core import serializers

def getAllRooms():
    rooms = list(Room.objects.all())
    random.shuffle(rooms)
    return rooms

def index(request):
    availableRooms = [];
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        date = request.POST['date']
        capacity = request.POST['capacity']
    
        rooms = getAllRooms();
        
        for room in rooms:
            r = Reservation.objects.filter(room = room.id)
            if len(r) == 0:
                availableRooms.append( room )
    
    else:
        availableRooms = getAllRooms()
    
    return render_to_response('index/index.html', {'availableRooms': availableRooms},
                               context_instance=RequestContext(request))


def getDict(room):
    return {'name':room.name, 'description':room.description, 'icon':room.icon, 'price':room.price, 'capacity':room.capacity, 'address':room.address, 'city':room.city, 'state':room.state, 'zip':room.zip, 'lat':room.lat, 'lon':room.lon}

def api(request):
    rooms = getAllRooms();
    s = simplejson.dumps([getDict(room) for room in rooms])

    data = serializers.serialize('json', Room.objects.all())
    return HttpResponse(data,'application/javascript')
    
#    return HttpResponse(s)
    
    

