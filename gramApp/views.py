from django.shortcuts import render, redirect
from .models import Image, Profile
from gramApp.forms import signupForm
from gramApp.tokens import account_activation_token

def home(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your instagram - Replica Account'
            message = render_to_string('account_activation_email')
    return render(request, 'index.html')


def userProfile(request):
    return render(request, 'profile.html')