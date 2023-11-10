from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    
    use_in_migrations = True
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('username', True)
        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    
    # dit is de UserModel.

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()


class Seeders(models.Model):
    
    temperatuur = models.FloatField()
    CO2  = models.IntegerField()
    luchtvochtigheid = models.IntegerField()
    luchtdruk = models.IntegerField()
    luchtkwaliteit = models.IntegerField()
    
    def save(self, *arg, **kwarg):
        self.temperatuur = round(self.temperatuur, 2)
        super(Seeders, self).save(*arg, **kwarg)
        
    
    
    
    