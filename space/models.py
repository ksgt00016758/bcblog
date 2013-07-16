#coding: utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    file = models.ImageField(u'图片', upload_to='static/images/photos/%Y/%m/%d')
    description = models.TextField(u'描述', null=True, blank=True)    
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    
    like = models.IntegerField(default=0,verbose_name=u'赞')
    likers = models.ManyToManyField(User)
    
    class Meta:
        db_table = 'photo'
        verbose_name = u'图片'
        verbose_name_plural = u'图片'
        ordering = ('-created_time', )
        
    def __unicode__(self):
        return '<Photo> %s' % self.file.path
