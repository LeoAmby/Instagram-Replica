from django.shortcuts import render, redirect
from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm, ImagePostForm
from gramApp.tokens import account_activation_token
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ImagePost, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request, f'Your account has been created successfully!')


        return redirect ('login')
    else:
        form = SignupForm()

    return render(request, 'register/register.html', {'form':form})

@login_required(login_url='signUp')
def home(request):
    photos = ImagePost.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user.profile
            image.save()
            return HttpResponseRedirect (request.path_info)

    else:
        form = ImagePostForm()
    params = {
        'photos': photos,
        'form': form,
        'users': users,
    }
    return render (request, 'index.html', params)


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)




@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})





# def login(response):
#     if response.method == 'POST':
#         form = LoginForm(response.POST)
#         if form.is_valid():
#             form.save()

#         return redirect ('profile')
#     else:
#         form = LoginForm()
#     return render(response, 'registration/login.html', {'form':form})