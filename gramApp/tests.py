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

    def delete_image(self):
        Image.image_name.remove(self)


class test_profile(TestCase):
    def setUp(self):
        self.photo = Profile(id = 'profilePhoto')
        self.bio = Profile(bio = 'bio')
    

    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Profile))
        self.assertTrue(isinstance(self.bio,Profile))


    def test_save(self):
        self.photo.save_image()
        self.assertTrue(Profile.name)

    def delete_profile(self):
        Profile.profile_profpic.remove(self)
        Profile.profile_bio.remove(self)