from django.db import models

class Profile(models.Model):
    profPic = models.Image(uplade_to = 'images/', blank = True, null=True)
    bio = models.Textfield()

    def __str__(self):
        return self.name

class Image(models.Models):
    photo = models.ImageField(upload_to = 'images/', blank = True, null=True  )
    name = models.CharField(max_len = 30)
    caption = models.CharField(max_len = 30)
    profile = models.ForeignKey(profile)
    comments = models.TextField()

    def __str__ (self):
        return self.profpic
