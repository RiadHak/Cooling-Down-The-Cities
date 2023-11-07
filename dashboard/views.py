from django.shortcuts import render, redirect
from .forms import RegisterFrom, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def signin(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = LoginForm()
        return render(request, "registration/login.html", {'form' : form})
    elif request.method == "POST":
        form = LoginForm(data=request.POST)
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        return render(request,'registration/login.html',{'form': form})

@login_required(login_url='/singin/')
def signout(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('signin')      

def signup(request):
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Registration successful!'
            return redirect('/signin')
        else:
            return render(request, 'registration/signup.html', {'form': form})

    form = RegisterFrom()
    return render(request, 'registration/signup.html', {'form':form})

def privatePolicy(request):
    return render(request, 'privatepolicy/privatepolicy.html')

@login_required(login_url='/signin/')
def dashboard(request):
    return render(request, 'dashboard.html')