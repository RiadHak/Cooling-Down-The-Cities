from django.shortcuts import render, redirect
from .forms import RegisterFrom, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def signin(request):
    # if request.method == "GET":
    #     if request.user.is_authenticated:
    #         return redirect('dashboard')
    #     form = LoginForm()
    #     return render(request, "signin.html", {'form' : form})
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print('test')
        if user is not None:
            print('login')
            login(request, user)
            return redirect('dashboard')
        return render(request,'registration/login.html',{'form': form})
    else:
        print('error')
        form = LoginForm()
        return render(request,'registration/login.html',{'form': form})



@login_required(login_url='/login/')
def signout(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')      

def signup(request):
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Registration successful!'
            return redirect('/login')
        else:
            return render(request, 'registration/signup.html', {'form':form})
    form = RegisterFrom()
    return render(request, 'registration/signup.html', {'form':form})

def privatePolicy(request):
    return render(request, 'privatepolicy/privatepolicy.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'index.html')