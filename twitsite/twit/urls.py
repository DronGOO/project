from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sport', views.sport, name = 'sport'),
    url(r'^it', views.it, name = 'it'),
    url(r'^stream', views.stream, name = 'stream'),
]