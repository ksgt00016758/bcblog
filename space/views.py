#coding: utf-8
import os
import settings
import logging
import datetime
import Image, ImageDraw, ImageFont
import simplejson as json

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django import shortcuts
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from jfu.http import upload_receive, UploadResponse, JFUResponse
from space.models import Photo, PhotoAlbum



LOG = logging.getLogger('bcblog')

def spaceHome(request):       
    
    photoAlbums = PhotoAlbum.objects.all()
    return shortcuts.render_to_response('space/index.html', 
    									{'STATIC_URL':settings.STATIC_URL,
                                         'photoAlbums':photoAlbums}, 
    									context_instance=RequestContext(request))

def beautifulHome(request):       
    
    photoAlbums = PhotoAlbum.objects.all()
    return shortcuts.render_to_response('space/beautiful.html', 
                                        {'STATIC_URL':settings.STATIC_URL,
                                         'photoAlbums':photoAlbums}, 
                                        context_instance=RequestContext(request))
def uploadHome(request):       

    return shortcuts.render_to_response('space/upload.html', 
                                        {'STATIC_URL':settings.STATIC_URL}, 
                                        context_instance=RequestContext(request))

@csrf_exempt
def uploadMeitu(request):

    file=request.FILES.get('Filedata',None) 
    print 'Begin' 
    name=request.POST['name']
    print name 
    ext_allowed = ['gif', 'jpg', 'jpeg', 'png']
    max_size = 2621440
    
    ext = file.name.split('.').pop()
    if ext not in ext_allowed:
        print '不是所要求的图片格式'
        json_data = {'result': '不是所要求的图片格式'}
        return HttpResponse(json.dumps(json_data), mimetype='application/json')
    #print('new_file1' + file.name)
    if file.size > max_size:
        print '===tada'
    #print('new_file12' + file.name)
    #if not os.path.isdir(save_path):
        #print('new_file2' + file.name)
        #os.makedirs(save_path)
    #print('new_file3' + ext)
    album_name = 'ablum1'
   
    try:
        photo_album =PhotoAlbum.objects.get(name=name)
    except (PhotoAlbum.DoesNotExist):
        print "photo_album.name Not exit"
    
    print photo_album.name
    photo = Photo.objects.create(file=file,
                         description="default",
                         photo_album=photo_album)

    json_data = {'result': '上传成功'}
    print 'save ok!'
    return HttpResponse(json.dumps(json_data), mimetype='application/json')
   

 
@require_POST
def upload( request ):

    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' will be a list of files.
  
    file = upload_receive( request )
    print('instance.file_field.file.name is [%s]', file.name)

    instance = Photo( file = file )
    instance.save()
    LOG.debug('instance.file_field.file.name is [%s]', settings.MEDIA_URL +instance.file.name)

    file_dict = {
        'name' : instance.file.name,
        'size' : instance.file.size,

        # The assumption is that file_field is a FileField that saves to
        # the 'media' directory.
        'url': '../' + instance.file.name,
        'thumbnail_url': '../' +instance.file.name,

        'delete_url': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'delete_type': 'POST',
    }

    return UploadResponse( request, file_dict )

@require_POST
def upload_delete( request, pk ):
    # An example implementation.
    success = True
    try:
        instance = Photo.objects.get( pk = pk )
        os.unlink( instance.file.path )
        instance.delete()
    except Photo.DoesNotExist:
        success = False

    return JFUResponse( request, success )    