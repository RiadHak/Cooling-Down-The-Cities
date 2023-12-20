from django.urls import path
from . import views 

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('privatepolicy/', views.privatePolicy, name='privatepolicy'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('getDataFromDB/', views.getDataFromDB, name='getDataFromDB'),
    path('get-humidity-data/', views.get_humidity_data, name='get_humidity_data'),
    path('get-aqi-data/', views.get_aqi_data, name='get_aqi_data'),
    path('get-temperature-data/', views.get_temperature_data, name='get_temperature_data'),
    path('get-co2-data/', views.get_co2_data, name='get_co2_data'),
    path('get-pressure-data/', views.get_pressure_data, name='get_pressure_data')


]