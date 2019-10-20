from django.db import models
from django.contrib.auth.models import User
import PIL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profPic = models.ImageField(default = 'avatar.png', upload_to='profile_pics/')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super(Profile, self).save()

        img = PIL.Image.open(self.profPic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profPic.path)

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



class ImagePost(models.Model):
    photo = models.ImageField(upload_to = 'images/', blank = True, null=True)
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

    
    