from django.conf.urls import url
from django.contrib.staticfiles.urls import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^kategorie/(?P<kat>(burgery|special|kalamary|prilohy|napoje))/$', views.kategorie, name='kategorie'),
	url(r'^produkt/(?P<pk>([0-9]+))/$', views.produkt, name='produkt'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)