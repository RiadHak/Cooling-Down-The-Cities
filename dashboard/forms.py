from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterFrom(forms.ModelForm):
    username = forms.CharField(
        validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(25)], 
        required=True, 
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    
    password = forms.CharField(
        validators=[validators.MinLengthValidator(5)], 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=65,
        validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(25)],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}) 
    )
    password = forms.CharField(
        max_length=256,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(25)], 
    )