from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .testoutput import cat
# import BlackJack
# import carddeck


# This allows variables to be passed into the html
def index(request):
	context = {'name': 'John', 'age': 13, 'height': 'tall'}
	return render(request, 'dumrun/dumrunhome.html', context)

def rules(request):
	return HttpResponse("Here is the dumrun test")