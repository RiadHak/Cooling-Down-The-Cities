from django.db import models

from .validators import *
# Create your models here.
class Register(models.Model):
    username  = models.CharField(max_length=25, unique=True)
    email     = models.EmailField(unique=True)
    password  = models.CharField(max_length=50)     
    class Meta:
        db_table = 'users'