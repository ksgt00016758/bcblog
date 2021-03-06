import os
import Image, ImageDraw, ImageFont
from django.test import TestCase
from space.models import Photo, PhotoAlbum
from django.core.urlresolvers import reverse

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

class SapceTest(TestCase):
    photo_path = os.path.join(LOCAL_PATH, '2.jpg')
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        im = Image.open(self.photo_path)
        print im.size
        width = 400
        ratio = float(width)/im.size[0]
        height = int(im.size[1]*ratio)
        nim = im.resize( (width, height), Image.BILINEAR )
        print nim.size
        nim.save( "resized.jpg" )
    
    def test_upload(self):
        photo_album = PhotoAlbum.objects.create(name='bruce')
        photo = Photo.objects.create(file=open(self.photo_path),
                         description="default",
                         photo_album=photo_album)