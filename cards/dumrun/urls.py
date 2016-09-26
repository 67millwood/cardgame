from django.conf.urls import url
from . import views


app_name = 'dumrun'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^test', views.rules, name='test'),
]