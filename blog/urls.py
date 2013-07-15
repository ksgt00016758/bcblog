from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('blog.views',
#    url('^$', 'home', name='home'),
    url('^(?P<post_id>\d+)/$', 'detail', name='post-detail'),
    url('^tag/(?P<tag_id>\d+)/$', 'list_by_tag', name='list-by-tag'),
)
