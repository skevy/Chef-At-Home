from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('cah.menus.views',
    url(r'^$', 'index'),
    url(r'^(?P<id>\d+)/$', 'detail', name="menu_detail"),
    url(r'^tags/(?P<slug>[\w\-]+)/$', 'by_tag', name="menus_by_tag"),
)
