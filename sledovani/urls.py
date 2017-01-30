from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.riders_list, name='riders_list'),
	url(r'^rider/(?P<pk>[0-9]+)/$', views.rider_detail, name='rider_detail'),
]