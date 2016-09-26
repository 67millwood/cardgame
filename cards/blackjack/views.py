from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return HttpResponse("Hello blackjack players")

def rules(request):
	return HttpResponse("Here are the rules")
	
def game(request):
	return render(request, 'blackjack/blackjackgame.html')
	# return HttpResponse("game page goes here")

def realgame(request):
	return render(request, 'blackjack/realblackjackgame.html')
	