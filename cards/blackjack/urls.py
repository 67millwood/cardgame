from django.conf.urls import url

from . import views

app_name = 'blackjack'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^rules', views.rules, name='rules'),
	url(r'game', views.game, name='game'),
	# url(r'^poker/$', views.poker, name='index')
]