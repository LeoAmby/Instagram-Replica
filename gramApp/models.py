from django.db import models

class Profile(models.Model):
    profPic = models.ImageField(upload_to = 'images/', blank = True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/', blank = True, null=True  )
    name = models.CharField(max_length = 30)
    caption = models.CharField(max_length = 30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    comments = models.TextField()

    def __str__ (self):
        return self.profpic
