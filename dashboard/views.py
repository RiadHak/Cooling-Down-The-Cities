from django.shortcuts import render, redirect
from .forms import RegisterFrom
from django.contrib import messages
from .validators import validation


def login(request):
    
    return render(request, 'login.html')
    
    
def signup(request):
    
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('/signup')
        else:
            form = RegisterFrom()
            username = request.POST.get('username')
            email = request.POST.get('email')
            checking = validation(username, email)
            _= [messages.error(request, x) for x in checking]              
            return render(request, 'signup.html', {'form':form})

    form = RegisterFrom()
    return render(request, 'signup.html', {'form':form})

def privatePolicy(request):
    
    return render(request, 'privatepolicy/privatepolicy.html')