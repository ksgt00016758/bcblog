from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('space.views',
#    url('^$', 'home', name='home'),
    url('^$', 'spaceHome', name='space-home'),
)
