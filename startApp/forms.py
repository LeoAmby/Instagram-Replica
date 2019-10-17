from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User
from gramApp.models import models

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