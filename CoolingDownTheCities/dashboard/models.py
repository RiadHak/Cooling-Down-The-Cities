from django.db import models
from django.core.validators import validate_email, validate_slug
# Create your models here.
class CustomUser(models.Model):
    username  = models.CharField(max_length=25)
    email     = models.EmailField(validators=[validate_email])
    password  = models.CharField(max_length=50)
    
    
    
