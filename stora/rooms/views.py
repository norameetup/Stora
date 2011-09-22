from django.template import Context, loader
from django.http import HttpResponse

def index(request):
	t = loader.get_template('rooms/index.html')
	c = Context({'nora_test':'hello_world',})

	return HttpResponse(t.render(c))
	#return HttpResponse( "hello there...")
