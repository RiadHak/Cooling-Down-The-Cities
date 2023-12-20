from django.shortcuts import render, redirect
from .forms import RegisterFrom, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Seeders
from django.utils import timezone
from datetime import timedelta
from django.db.models import Avg


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

@login_required(login_url='/signin/')
def signout(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('/signin')      

def signup(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('dashboard')
    elif request.method == "POST":
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

def getDataFromDB(request):
    mydata = Seeders.objects.values().last() 
    return JsonResponse({'data': list(mydata.values())})

def get_humidity_data(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    humidity_data = Seeders.objects.filter(
        timestamp__range=(start_date, end_date)
    ).values('timestamp', 'luchtvochtigheid')

    return JsonResponse({'humidity_data': list(humidity_data)})

def get_aqi_data(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    aqi_data = Seeders.objects.filter(
        timestamp__range=(start_date, end_date)
    ).values('timestamp', 'luchtkwaliteit')

    return JsonResponse({'aqi_data': list(aqi_data)})

def get_temperature_data(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    temperature_data = Seeders.objects.filter(
        timestamp__range=(start_date, end_date)
    ).values('timestamp', 'temperatuur')

    return JsonResponse({'temperature_data': list(temperature_data)})

def get_pressure_data(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    pressure_data = Seeders.objects.filter(
        timestamp__range=(start_date, end_date)
    ).values('timestamp', 'luchtdruk')

    return JsonResponse({'pressure_data': list(pressure_data)})

def get_co2_data(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    co2_data = Seeders.objects.filter(
        timestamp__range=(start_date, end_date)
    ).values('timestamp', 'co2')

    return JsonResponse({'co2_data': list(co2_data)})