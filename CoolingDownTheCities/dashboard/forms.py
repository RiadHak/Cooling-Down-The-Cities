from django import forms
from .models import CustomUser


class registerPanel(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = '__all__'
    