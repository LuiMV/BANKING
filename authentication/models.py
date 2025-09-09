from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100, unique=True)  
    password = models.CharField(max_length=128)  
    id_city = models.IntegerField()
    status = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
    deleted_at = models.DateTimeField(null=True, blank=True)  

class Cities(models.Model):
    id_departament = models.BigIntegerField()
    name = models.CharField(max_length = 20)
    abrev = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Departaments(models.Model):
    name = models.CharField(max_length = 20)
    abrev = models.CharField(max_length = 20)
    id_country = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank= True)

class Countries(models.Model):
    name = models.CharField(max_length = 20)
    abrev = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
