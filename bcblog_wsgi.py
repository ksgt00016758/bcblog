import os
import sys
 
#substitute mysite with the name of your project !!!
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
 
path = os.path.dirname(os.path.realpath(__file__))
if path not in sys.path:
    sys.path.insert(0, path)
    sys.path.insert(1, os.path.join(path, '..'))
 
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
