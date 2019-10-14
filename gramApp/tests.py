from django.test import TestC
from .models import Image, Profile

class ImageTest(TestCase):
    def setUp(self):
        self.photo = Image(id = 'profilePhoto')
    

    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Image))

    
    def test_save(self):
        self.photo.save_image()
        self.assertTrue(Image.name)

    def test_delete():
        self.image.delete_image()
        self.assertTrue(Image.name)