from django.db import models
from django.utils.encoding import smart_unicode


class Tag(models.Model):
    name = models.CharField(max_length=256)
    order = models.PositiveIntegerField(default=10)
    
    class Meta:
        db_table = 'tag'
        ordering = ('order',)
            
    def __unicode__(self):
        return smart_unicode(self.name)
    

class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, db_table='article_tag_map')
    is_valid = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=10)
    
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'article'
        ordering = ('order', '-last_modified',)
        
    def __unicode__(self):
        return smart_unicode(self.title)
