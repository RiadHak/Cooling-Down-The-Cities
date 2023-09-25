from django.shortcuts import render

def login(request):
    
    return render(request, 'login.html')

def signup(request):
    
    return render(request, 'signup.html')

def privatePolicy(request):
    
    return render(request, 'privatepolicy/privatepolicy.html')
