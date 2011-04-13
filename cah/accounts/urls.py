from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('cah.accounts.views',
    url(r'^$', 'index'),
    url(r'^signup/$', 'signup'),
    url(r'^signup/success/$', 'signup_success', name="signup_success"),
    url(r'^signout/$', 'signout'),
)

urlpatterns += patterns('',
    url(r'^signin/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/signin.html'}, name="signin"),
    url(r'^auth/', include('social_auth.urls')),
)
