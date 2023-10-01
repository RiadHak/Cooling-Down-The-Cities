from django.shortcuts import render, redirect
from .forms import RegisterFrom
from django.contrib import messages
from .models import Register


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
            return render(request, 'signup.html', {'form':form})
    form = RegisterFrom()
    return render(request, 'signup.html', {'form':form})

def privatePolicy(request):
    
    return render(request, 'privatepolicy/privatepolicy.html')