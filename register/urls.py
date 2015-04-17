from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('', 
    url(r'^player/$', views.players_list),
    url(r'^player/pay_status/$', views.players_pay_status),
    url(r'^player/(?P<pk>[0-9]+)/$', views.player_detail),
    url(r'^player/new/$', views.player_new, name='player_new'),
    url(r'^player/(?P<pk>[0-9]+)/edit/$', views.player_edit, name='player_edit'),
    url(r'^player/(?P<pk>[0-9]+)remove/$', views.player_remove, name='player_remove'),
    url(r'^sponsor/$', views.sponsor_list),
    url(r'^sponsor/(?P<pk>[0-9]+)/$', views.sponsor_detail),
    url(r'^sponsor/new/$', views.sponsor_new, name='sponsor_new'),
    url(r'^sponsor/bronze/$', views.sponsor_bronze, name='sponsor_bronze'),
    url(r'^sponsor/silver/$', views.sponsor_silver, name='sponsor_silver'),
    url(r'^sponsor/gold/$', views.sponsor_gold, name='sponsor_gold'),
    url(r'^sponsor/platinum/$', views.sponsor_platinum, name='sponsor_platinum'),
    url(r'^sponsor/(?P<pk>[0-9]+)/edit/$', views.sponsor_edit, name='sponsor_edit'),
    url(r'^sponsor/(?P<pk>[0-9]+)remove/$', views.sponsor_remove, name='sponsor_remove'),

)