from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with that email already exists in our database. Please choose a different email or login.")
            return redirect("register")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match. Please try again.")
            return redirect("register")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")

        
    
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("login")
        
        print(username, password)
    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')

def logoutaction(request):
    logout(request)
    return redirect("login")


    
