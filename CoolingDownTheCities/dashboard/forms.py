from django import forms
from .models import Register
class RegisterFrom(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        } 
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }    
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    class Meta:
        model = Register
        fields = ('username', 'email', 'password')
        
        
    