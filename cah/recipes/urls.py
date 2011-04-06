from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('cah.recipes.views',
    url(r'^$', 'index'),
    url(r'^(?P<id>\d+)/$', 'detail', name="recipe_detail"),
    url(r'^tags/(?P<slug>[\w\-]+)/$', 'by_tag', name="recipes_by_tag"),
    url(r'^add/$', 'add', name="add_recipe"),
)
