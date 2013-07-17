#coding: utf-8
import datetime
import os


from django.db import models
from django.contrib.auth.models import User

import Image, ImageDraw, ImageFont
import settings

# Create your models here.
class Photo(models.Model):
    file = models.ImageField(u'图片', upload_to='static/images/photos/')
    thumbs_file = models.TextField(u'图片', null=True, blank=True)
    description = models.TextField(u'描述', null=True, blank=True)    
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    photo_album = models.ForeignKey('space.PhotoAlbum', verbose_name=u'相册')
    
    like = models.IntegerField(default=0,verbose_name=u'赞')
    #likers = models.ManyToManyField(User)
    
    class Meta:
        db_table = 'photo'
        verbose_name = u'图片'
        verbose_name_plural = u'图片'
        ordering = ('-created_time', )
        
    def __unicode__(self):
        return '<Photo> %s' % self.file.path
    def save(self, **keys):
        now = datetime.datetime.now()
        fileName = now.strftime("%Y%m%d%H%M%S")
        self.file.name = fileName + '.jpg'
        self.thumbs_file = "/static/images/photos/thumbs/" + fileName + '.jpg'
        super(Photo, self).save()
        im = Image.open(self.file)
        print im.size
        
        width = im.size[0]
        height = im.size[1]
        min_width = 140
        min_height = 93
        if(width<=height):
            min_height = 140
            min_width = 93
            width = 426
            height = 600
        else:
            width = 600
            height = 426
        ori = im.resize( (width, height), Image.BILINEAR )
        nim = im.resize( (min_width, min_height), Image.BILINEAR )
        print nim.size
        nim.save( os.path.join(settings.PHOTO_REPO+'thumbs/', fileName+'.jpg') )
        ori.save( os.path.join(settings.PHOTO_REPO, fileName+'.jpg') )

        print 'save the model'


class PhotoAlbum(models.Model):
    name = models.TextField(u'相册名', null=True, blank=True)
    description = models.TextField(u'描述', null=True, blank=True)    
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    
    class Meta:
        db_table = 'photo_album'
        verbose_name = u'相册名'
        verbose_name_plural = u'相册名'
        ordering = ('-created_time', )
        
    def __unicode__(self):
        return '<name> %s' % self.name
