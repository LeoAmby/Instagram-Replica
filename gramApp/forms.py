from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'password1', 'password2')

class loginForm(forms.Forms):
    username = forms.CharField()
    password = forms.CharField()