from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    phone=models.IntegerField(max_length=10)