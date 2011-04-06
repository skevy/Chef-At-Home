from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('cah.recipes.views',
    url(r'^$', 'index'),
    url(r'^2/$', 'detail'),
    url(r'^add/$', 'add'),
)
