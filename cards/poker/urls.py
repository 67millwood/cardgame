from django.conf.urls import url

from . import views

app_name = 'poker'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'game', views.game, name='game'),
	# url(r'home', views.home, name='home')
]