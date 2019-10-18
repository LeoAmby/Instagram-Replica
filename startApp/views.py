from django.shortcuts import render, redirect
from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm
from gramApp.models import Image, Profile
from gramApp.tokens import account_activation_token
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signUp(response):
    if response.method == 'POST':
        form = SignupForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfully!')


        return redirect ('login')
    else:
        form = SignupForm()

    return render(response, 'register/register.html', {'form':form})


def home(request):
    return render (request, 'index.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                    instance=request.user.profile)
    
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)



# def login(response):
#     if response.method == 'POST':
#         form = LoginForm(response.POST)
#         if form.is_valid():
#             form.save()

#         return redirect ('profile')
#     else:
#         form = LoginForm()
#     return render(response, 'registration/login.html', {'form':form})