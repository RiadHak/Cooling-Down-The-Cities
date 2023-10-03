from django import forms
from .models import Register
from django.core import validators

class RegisterFrom(forms.Form):
    username = forms.CharField(
        validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(25)], 
        required=True, 
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    
    password = forms.CharField(
        validators=[validators.MinLengthValidator(5)], 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    
    
    
    class Meta:
        model = Register
        fields = ('username', 'email', 'password')
        
    
        
        
        
    