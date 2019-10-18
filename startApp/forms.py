from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User
# from gramApp.models import models
from startApp.models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(UserCreationForm):
    username = forms.CharField(max_length = 30)

    class Meta:
        model = User
        fields = ["username", "email"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profPic"]