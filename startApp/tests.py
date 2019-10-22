from django.test import TestCase
from .models import ImagePost, Profile

# Create your tests here.
class ImagePostTest(Testcase):
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,ImagePost))
    
    
    def test_save(self):
        self.photo.save_image()
        self.assertTrue(ImagePost.name)


    def setUp(self):
        self.siblings = Profile(name = 'siblings')


    def delete_image(self):
        ImagePost.image_name.remove(self)

  
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
