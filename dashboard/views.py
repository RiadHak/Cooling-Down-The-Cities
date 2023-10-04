from django.shortcuts import render, redirect
from .forms import RegisterFrom
from django.contrib import messages
from .models import Register
from argon2 import PasswordHasher

def login(request):
    
    return render(request, 'login.html')
    
def signup(request):
    
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            Pw_hasher = PasswordHasher()
            pw = form.cleaned_data.get('password')
            hash_pw = Pw_hasher.hash(pw).encode('utf-8')
            instance = form.save(commit=False)
            instance.password = hash_pw
            instance.save()
            messages.success(request, 'Registration successful!')
            return redirect('/signup')
        else:
            return render(request, 'signup.html', {'form':form})
    form = RegisterFrom()
    return render(request, 'signup.html', {'form':form})


def privatePolicy(request):
    path = 'privatepolicy/privatepolicy.html'
    return render(request, path)