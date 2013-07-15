from datetime import datetime
import pytz

from django import template
from django.conf import settings

from common import LOG

register = template.Library()


LOCAL_TIME_ZONE = pytz.timezone(settings.TIME_ZONE)

def utc2local(utc_datetime, utc_format='%Y-%m-%dT%H:%M:%SZ'):
    '''
    The DateTime format of UTC is not the same even in the same OpenStack:
        - instance: %Y-%m-%dT%H:%M:%SZ
        - volume: %Y-%m-%d %H:%M:%S
        - swift: %Y-%m-%dT%H:%M:%S.%f (eg: 2012-06-26T08:44:09.557970)
    '''
    try:
        if isinstance(utc_datetime, unicode) or isinstance(utc_datetime, str):
            utc_datetime = datetime.strptime(utc_datetime.replace(' ', ''), utc_format)
            
        utc_dt = pytz.utc.localize(utc_datetime)
        local_dt = LOCAL_TIME_ZONE.normalize(utc_dt.astimezone(LOCAL_TIME_ZONE))
        
        return local_dt
    except Exception, e:
        LOG.error(e)
        return utc_datetime
    
register.filter('utc2local', utc2local)


def local2utc(local_datetime, no_tz=True):
    '''
    This is just a util function, not for filter usage.
    '''
    local_datetime = LOCAL_TIME_ZONE.localize(local_datetime)
    utc_datetime = pytz.utc.normalize(local_datetime.astimezone(pytz.utc))
    
    if no_tz:
        utc_datetime = utc_datetime.replace(tzinfo=None)
    
    return utc_datetime
