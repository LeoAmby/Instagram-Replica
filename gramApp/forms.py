from django import forms

class signupForm(forms.Form):
    fullname = forms.CharField
    username = forms.CharField()
    email = forms.EmailField()

class loginForm(forms.Forms):
    username = forms.CharField()
    password = forms.CharField()