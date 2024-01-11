from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserAuthenticationForm
from blog.models import Category

def index(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'authentication/index.html')

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    categories = Category.objects.all()

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            user_form = UserRegistrationForm()
    else:
        user_form = UserRegistrationForm()
    
    context = {
        "user_form": user_form,
        "categories": categories,
    }
    return render(request, 'authentication/registration.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    categories = Category.objects.all()

    if request.method == 'POST':
        form = UserAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')
            else:
                # Handle inactive user or invalid credentials
                return render(request, 'authentication/login.html', {'error_message': 'Invalid login credentials or inactive account'})
    else:
        form = UserAuthenticationForm()
    
    context = {
        "form": form,
        "categories": categories,
    }

    return render(request, 'authentication/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'authentication/home.html', context)

