from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('', 
    url(r'^$', views.players_list),
    url(r'^player/(?P<pk>[0-9]+)/$', views.player_detail),
    url(r'^player/new/$', views.player_new, name='player_new'),
    url(r'^player/(?P<pk>[0-9]+)/edit/$', views.player_edit, name='player_edit'),
)