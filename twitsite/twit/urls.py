from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sport', views.sport, name = 'sport'),
    url(r'^it', views.it, name = 'it'),
    url(r'^showbiz', views.showbiz, name = 'showbiz'),
    url(r'^social', views.social, name = 'social'),
    url(r'^game', views.game, name = 'game'),
    url(r'^auto', views.auto, name = 'auto'),
    url(r'^robots.txt$', views.robots, name = 'robots.txt'),
    url(r'^sitemap.xml$', views.sitemap, name = 'sitemap.xml'),

]

handler404 = views.page404
handler403 = views.page403
handler500 = views.page500