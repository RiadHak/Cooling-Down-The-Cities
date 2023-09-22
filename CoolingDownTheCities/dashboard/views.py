from django.shortcuts import render

def login(request):
    
    name = 'Enes'
    context = {
        'D': name
    }
    
    return render(request, 'login.html', context)
