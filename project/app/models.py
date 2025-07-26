from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    phone=models.IntegerField(max_length=10)
    
class Add_To_Cart(models.Model):
    image=models.ImageField(upload_to="images/")
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField()
    # product_quantity=models.IntegerField()
    
class CareersQuery(models.Model):
    your_name=models.CharField(max_length=20)
    email_address=models.EmailField(max_length=20)
    age=models.IntegerField()
    job_description=models.TextField(max_length=50)