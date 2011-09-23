from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from rooms.models import Room, Reservation
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

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

def search(request):
    
    if request.method == "POST":
        print 'dude'
    
    zipcode = request.POST['zipcode']
    date = request.POST['date']
    capacity = request.POST['capacity']
    
    rooms = getAllRooms();
    
    availableRooms = [];
    for room in rooms:
        r = Reservation.objects.filter(room = room.id)
        print r
        if len(r) == 0:
            print 'no res!'
            availableRooms.append( room )
    
        
    return render_to_response('index/index.html', {'availableRooms': availableRooms},
                               context_instance=RequestContext(request))

