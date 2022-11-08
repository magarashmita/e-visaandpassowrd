from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Visaform(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Gender = (('male',"Male"),
                ('female',"Female"),
                ('other',"Other"))
    Gender = models.CharField(max_length=10,choices=Gender,default="male")




class Passportform(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Gender = (('male',"Male"),
                ('female',"Female"),
                ('other',"Other"))
    Gender = models.CharField(max_length=10,choices=Gender,default="male")
