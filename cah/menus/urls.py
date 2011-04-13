from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from cah.menus.models import Menu

urlpatterns = patterns('cah.menus.views',
    url(r'^$', 'index'),
    url(r'^add/$', 'add', name="menu_create"),
    url(r'^(?P<id>\d+)/remove_recipe/(?P<recipe_id>\d+)/$', 'remove_recipe', name="menu_remove_recipe"),
    url(r'^(?P<id>\d+)/add_recipe/(?P<recipe_id>\d+)/$', 'add_recipe', name="menu_add_recipe"),
    url(r'^(?P<id>\d+)/$', 'detail', name="menu_detail"),
    url(r'^tags/(?P<slug>[\w\-]+)/$', 'by_tag', name="menus_by_tag"),
)

urlpatterns += patterns('',
    url(r'^favorites/$', 'cah.utils.favorited_items', { 'model': Menu }, name="favorited_menus")
)
