from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
 
def validate_email(value):
    
    if User.objects.filter(email = value).exists():
        raise ValidationError(
            (f"{value} is already used for another account."),
            params = {'value': value}
        )
        
def validate_username(value):
    
    if not User.objects.filter(username = value).exists():
        raise ValidationError(
            (f"There is no user with \'{value}\' username, Please try again."),
            params = {'value': value}
        )
