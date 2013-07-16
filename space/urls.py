from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('space.views',
#    url('^$', 'home', name='home'),
    url( '^$', 'spaceHome', name='space-home' ),
    url( '^beautiful/$', 'beautifulHome', name='beautiful-home' ),
   	url( r'upload/', 'upload', name='jfu_upload' ),
   	url( r'^delete/(?P<pk>\d+)$', 'upload_delete', name = 'jfu_delete' ),
    url( r'uploadMeitu/', 'uploadMeitu', name='upload-meitu' ),
)
