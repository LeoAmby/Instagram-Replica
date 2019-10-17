from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    profPic = models.ImageField(upload_to = 'images/', blank = True, null=True)
    bio = models.TextField()
    email_confirmed = models.BooleanField(default=False)


    @receiver(post_save, sender=User)
    def update_user_profile(self, sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/', blank = True, null=True  )
    name = models.CharField(max_length = 30)
    caption = models.CharField(max_length = 30)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,)
    comments = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__ (self):
        return self.name

    
    def __unicode__(self):
        return self.name
        
    def save_image(self):
        self.save()

    def update_image(self):
        self.update()

    def delete_image(self):
        self.delete()

    
