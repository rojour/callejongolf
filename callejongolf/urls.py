from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),
    url(r'^players$', 'home.views.players'),
    url(r'^sponsors$', 'home.views.sponsors'),
    url(r'^contactus$', 'home.views.contactus'),
    url(r'^management$', 'home.views.management'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'', include('register.urls')),
)
