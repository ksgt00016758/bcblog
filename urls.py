from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

from django import template
template.add_to_builtins('django.templatetags.i18n')
template.add_to_builtins('common.templatetags.mytags')

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url('^search/$', 'blog.views.search', name='search'),
    url(r'^post/', include('blog.urls')),
    
#    url(r'^about/$', 'django.views.generic.simple.direct_to_template', {'template': 'about.html'}, name='about'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^space/', include('space.urls')),
    url(r'crossdomain.xml$',direct_to_template, {'template': 'crossdomain.xml', 'mimetype': 'text/plain'}),

)
