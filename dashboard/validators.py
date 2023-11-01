from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import CustomUser

def validate_email(value):
    
    if CustomUser.objects.filter(email = value).exists():
        raise ValidationError(
            (f"{value} is already used for another account."),
            params = {'value': value}
        )
        
def validate_username(value):
    
    if not CustomUser.objects.filter(email = value).exists():
        raise ValidationError(
            (f"There is no user with the email \'{value}\', Please try again."),
            params = {'value': value}
        )
