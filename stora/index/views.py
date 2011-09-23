from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from rooms.models import Room, Reservation
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.utils import simplejson

def getAllRooms():
    rooms = Room.objects.all()
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

#    description = models.TextField()
#    icon = models.TextField(max_length=200)
#    price = models.IntegerField()
#    capacity = models.IntegerField()
#    address = models.CharField(max_length=200)
#    city = models.CharField(max_length=100)
#    state = models.CharField(max_length=20)
#    zip = models.IntegerField()
#    lat = models.FloatField()
#    lon = models.FloatField()
def getDict(room):
    return {'name':room.name, 'description':room.description, 'icon':room.icon, 'price':room.price, 'capacity':room.capacity, 'address':room.address, 'city':room.city, 'state':room.state, 'zip':room.zip, 'lat':room.lat, 'lon':room.lon}

def api(request):
    rooms = list(getAllRooms());
    s = simplejson.dumps([getDict(room) for room in rooms])

    return HttpResponse(s)
    
    

