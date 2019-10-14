from django.shortcuts import render
from .models import Image, Profile

def home(request):
    return render(request, 'index.html')


def userProfile(request):
    return render(request, 'profile.html')