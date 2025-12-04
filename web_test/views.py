from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def homepage(request):
    """Homepage view that shows the main website"""
    return render(request, "web.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('login')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('login')
        else:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('homepage')

    return render(request, "login2.html")

def Registar(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose another.')
            return redirect('register')

        # Create user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        
        # Auto login after registration
        login(request, user)
        messages.success(request, f'Account created successfully! Welcome, {first_name}!')
        return redirect('homepage')

    return render(request, "register2.html")

def log_out(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')