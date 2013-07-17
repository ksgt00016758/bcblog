from django.contrib import admin

from space.models import Photo, PhotoAlbum


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('file', 'created_time')


class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)
