import email
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import CharField, EmailField, IntegerField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    is_librarian=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

class meta:
    swappable='AUTH_USER_MODEL'

class Contact(models.Model): # So let,s understand what is happening here.So when a person visits on your site and filled the contact us form and submit it then you need that user details which he filled in the form so for this task you have to create models. In this model class "contact" mean a table name called contact is created and it,s column names are "name ","email","phone".But after doing all this you need to apply migration but before applying migrations you need to register your model in admin.py file.Basically migration create a file which stores all the changes defined in your model.After all this run migrate command which actual creates that table named "contact"
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=120)
    phone=models.IntegerField()
    desc=models.CharField(max_length=300)
    
    def __str__(self): #this function we used for save details by name in database
        return self.name
class Book(models.Model):
    book_id=models.AutoField(primary_key=True,unique=True)
    book_isbn=models.CharField(max_length=10)
    book_name=models.CharField(max_length=100)
    pub_date=models.DateField()
    book_price=models.IntegerField()
    book_des=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to='images',default="")

    def __str__(self): #this function we used for save details by name in databas
        return self.book_name
class Order(models.Model):
    cust_name=models.CharField(max_length=100,null=True)
    cust_phone=models.IntegerField()
    cust_email=models.EmailField(max_length=120)
    cust_date=models.DateField(null=True)
    days=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(60)])

    def __str__(self): #this function we used for save details by name in databas
        return self.cust_email
class Return1(models.Model):
    cust1_name=models.CharField(max_length=100)
    cust1_email=models.EmailField(max_length=120)
    cust1_phone=models.IntegerField(blank=True,null=True)
    ret_book_name=models.CharField(max_length=100)  
    ret_date=models.DateField()

    def __str__(self):
        return self.cust1_name
    

