from django.shortcuts import render, redirect
from .forms import SignupForm
from gramApp.models import Image, Profile
from gramApp.tokens import account_activation_token
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 

def signUp(response):
    if response.method == 'POST':
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect ('/signup')
    else:
        form = SignupForm()

    return render(response, 'register/register.html', {'form':form})
