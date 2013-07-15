from django.contrib import admin

from common import LOG
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'is_valid', 'created')
    
    filter_horizontal = ('tags',)
    
admin.site.register(Article, ArticleAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
admin.site.register(Tag, TagAdmin)
