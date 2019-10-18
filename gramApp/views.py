# from django.shortcuts import render, redirect
# from .models import Image, Profile
# from gramApp.forms import signupForm
# from gramApp.tokens import account_activation_token
# from django.http import HttpResponse, Http404
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm 


# def home(request):
#     if request.method == 'POST':
#         form = signupForm(request.POST)
#         if form.is_valid():
#         #     user = form.save(commit=False)
#         #     user.is_active = False
#             form.save()
#             # current_site = get_current_site(request)
#             # subject = 'Activate Your instagram - Replica Account'
#         return redirect('home')
   
#     else:
#         form = signupForm()
#     return render(request, 'index.html')


# def userProfile(request):
#     return render(request, 'profile.html')