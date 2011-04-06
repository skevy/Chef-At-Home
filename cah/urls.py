from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cah.views.index'),
    url(r'^menus/', include('cah.menus.urls')),
    url(r'^meal-plans/', include('cah.meal_plans.urls')),
    url(r'^recipes/', include('cah.recipes.urls')),

    url(r'^account/auth/', include('social_auth.urls')),
    url(r'^account/logout/$', 'cah.views.logout'),

    url(r'^search/$', 'cah.views.search'),

    # ADMIN
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if getattr(settings, 'STAGING_SERVER', None) or getattr(settings, 'LOCAL_DEV', None):
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )