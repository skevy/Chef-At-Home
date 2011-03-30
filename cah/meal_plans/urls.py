from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('cah.meal_plans.views',
    url(r'^$', 'index'),
)
