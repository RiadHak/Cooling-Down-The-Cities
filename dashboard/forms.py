from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from .models import CustomUser
from .validators import *

class RegisterFrom(UserCreationForm):
    email = forms.EmailField(required=True, validators=[validate_email])
    
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['username'].help_text= ''

class LoginForm(AuthenticationForm):
    username = forms.EmailField(required=True, validators=[validate_username])
    class Meta:
        model = CustomUser
        fields = ['email','password']
