import simplejson as json

from django.http import HttpResponse
from django.views.generic import View
from django.http import QueryDict
from django import shortcuts

from common import LOG


def index(request):
    LOG.debug('request.user is [%s]', request.user)
    return shortcuts.render_to_response('index.html', {'request':request})


class JsonView(View):
    def __init__(self, **kwargs):
        super(JsonView, self).__init__(**kwargs)
        
        self.json_data = {'result': '0'}
         
        
    def json(self, extra_data=None):
        if extra_data is not None:
            self.extra(extra_data)
        return HttpResponse(json.dumps(self.json_data), mimetype='application/json')
    
    
    def error(self, error_dict_or_str=''):
        self.json_data = {'result': '1', 'errors': error_dict_or_str}
        return self.json()
    
    
    def extra(self, dict_data):
        self.json_data.update(dict_data)
        
    
    def delete(self, request):
        request.DELETE = QueryDict(request.body)
        
    
    def put(self, request):
        '''
        Load request data into request.PUT
        refs: https://bitbucket.org/jespern/django-piston/src/c4b2d21db51a/piston/utils.py
        '''
        if hasattr(request, '_post'):
            del request._post
            del request._files
        
        try:
            request.method = 'POST'
            request._load_post_and_files()
            request.method = 'PUT'
        except AttributeError, e:
            LOG.exception(e)
            request.META['REQUEST_METHOD'] = 'POST'
            request._load_post_and_files()
            request.META['REQUEST_METHOD'] = 'PUT'
            
        request.PUT = request.POST
        

class SampleRestView(JsonView):
    def get(self, request):
        LOG.debug('GET - request.GET : %s', request.GET)
        return self.json(request.GET.dict())
    
    def post(self, request):
        LOG.debug('POST - request.POST : %s', request.POST)
        return self.json(request.POST.dict())
    
    def delete(self, request):
        super(SampleRestView, self).delete(request)
        LOG.debug('DELETE - request.DELETE : %s', request.DELETE)
        return self.json(request.DELETE.dict())
    
    def put(self, request):
        super(SampleRestView, self).put(request)
        LOG.debug('PUT - request.PUT : %s', request.PUT)
        return self.json(request.PUT.dict())
    