from django.shortcuts import render
from .forms import registerPanel
def login(request):
    
    return render(request, 'login.html')

def signup(request):
    
    if request.method == "POST":
        form = registerPanel(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, 'signup.html', form)
        else:
            pass
    return render(request, 'signup.html')
            
def privatePolicy(request):
    
    return render(request, 'privatepolicy/privatepolicy.html')
