from django.db import models
from django.db.models import Model
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserRoles(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.role_name


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    user_role = models.ForeignKey(UserRoles, on_delete=models.CASCADE, related_name='users')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_users')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_role(self):
        return self.user_role.role_name


class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)


class AirlineCompanies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE, to_field='id') 
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='id') 


class Flights(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)                    
    airline_company_id = models.ForeignKey(AirlineCompanies, on_delete=models.CASCADE, to_field='id')  
    origin_country_id = models.ForeignKey(Countries, on_delete=models.CASCADE, to_field='id', related_name='origin_country_id')  
    destination_country_id = models.ForeignKey(Countries, on_delete=models.CASCADE, to_field='id', related_name='destination_country_id') 
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    remaining_tickets = models.IntegerField(default=0)


class Customers(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    credit_card_number = models.CharField(max_length=20, unique=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='id')  


class Tickets(models.Model):
    id = models.BigAutoField(primary_key=True)
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE, to_field='id')  
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, to_field='id') 


class Adminstrators(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='id')