from django.shortcuts import HttpResponse
from django.shortcuts import render

# from .models import Question

def index(request):
	return HttpResponse("Hello poker players") 

def game(request):
    return render(request, 'poker/pokerhome.html')