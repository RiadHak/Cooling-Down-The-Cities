from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
import re

def Validate_email(value):

    if validate_email(value):
        raise ValidationError('not a valid email')
    return value

# def Validate_username(value):
#     regex = ['0-9']
#     if value > 25 and :
#         raise ValidationError('Username is to ')

    