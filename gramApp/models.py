from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profPic = models.ImageField(upload_to = 'images/', blank = True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/', blank = True, null=True  )
    name = models.CharField(max_length = 30)
    caption = models.CharField(max_length = 30)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,)
    comments = models.TextField()

    def __str__ (self):
        return self.profp
        
    def save_image(self):
        self.save()

    def update_image(self):
        self.update()

    def delete_image(self):
        self.delete()

    
