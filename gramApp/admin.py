from django.contrib import admin
from gramApp.models import Profile, Image


class ProfileAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, ImageAdmin)