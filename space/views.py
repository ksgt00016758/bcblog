from django import shortcuts
from django.template import RequestContext
from django.core.urlresolvers import reverse

def spaceHome(request):       
    return shortcuts.render_to_response('space/index.html')
    