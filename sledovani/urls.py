from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.riders_list, name='riders_list'),
]