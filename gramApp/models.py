from django.db import models

class Image(models.Models):
    photo = models.ImageField(upload_to = 'images/', blank = True, null=True  )
    name = models.CharField(max_len = 30)
    caption = models.CharField(max_len = 30)
    profile = models.ForeignKey(profile)
    comments = models.TextField()