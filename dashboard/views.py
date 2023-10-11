from django.shortcuts import render, redirect
from .forms import RegisterFrom, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .validators import HashPW

def signin(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = LoginForm()
        return render(request, "signin.html", {'form' : form})
    
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                print('success')
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, f'Invalid email or password')
                return render(request,'signin.html',{'form': form})
    return render(request, 'signin.html')

@login_required(login_url='/signin/')
def signout(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('signin')      

def signup(request):
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            pw = form.cleaned_data.get('password')
            hash_pw = HashPW(pw)
            instance = form.save(commit=False)
            instance.password = hash_pw
            instance.save()
            messages = 'Registration successful!'
            return redirect('/signin')
        else:
            return render(request, 'signup.html', {'form':form})
    form = RegisterFrom()
    return render(request, 'signup.html', {'form':form})

def privatePolicy(request):
    return render(request, 'privatepolicy/privatepolicy.html')

@login_required(login_url='/signin/')
def dashboard(request):
    return render(request, 'index.html')