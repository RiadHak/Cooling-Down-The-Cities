from django.shortcuts import render, redirect
from .forms import RegisterFrom
def login(request):
    
    return render(request, 'login.html')

def signup(request):
    
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            form = RegisterFrom()
            return render(request, 'signup.html', {'form':form})
        
    form = RegisterFrom()
    return render(request, 'signup.html', {'form':form})
        
    

def privatePolicy(request):
    
    return render(request, 'privatepolicy/privatepolicy.html')