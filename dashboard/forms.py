from django import forms
from .models import Register
from django.core.exceptions import ValidationError


class RegisterFrom(forms.ModelForm):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    class Meta:
        model = Register
        fields = ('username', 'email', 'password')
        
        
    