from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.riders_list, name='riders_list'),
	url(r'^rider/(?P<pk>\d+)/$', views.rider_detail, name='rider_detail'),
]