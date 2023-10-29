from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .validators import *

class RegisterFrom(UserCreationForm):
    email = forms.EmailField(required=True, validators=[validate_email])
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, validators=[validate_username])
    class Meta:
        model = User
        fields = ['password']
