# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Login(models.Model):
    name = models.EmailField()
    pswrd = models.CharField(max_length=16)

class endUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enduser_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/', null=True)
    phone = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class QNA(models.Model):
    questions = models.CharField(max_length=1000)
    answers = models.CharField(max_length=10000)
    
class Index_gmails(models.Model):
    emails = models.EmailField()

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation_id = models.AutoField(primary_key=True)
    organisation_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True)
    phone = models.IntegerField(null=True)
    # Address section
    street = models.CharField(max_length=400, null=True, default="")
    city = models.CharField(max_length=400, null=True, default="")
    state = models.CharField(max_length=400, null=True, default="")
    zipcode = models.CharField(max_length=400, null=True, default="")
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.CharField(max_length=3000)

class RecycleForm(models.Model):
    order_id = models.CharField(max_length=100, primary_key=True)
    user_id = models.CharField(max_length=100, default=1, null=True)
    organisation_id = models.CharField(max_length=100, default=1, null=True)
    item_type = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='recycle_images/', null=True)
    location = models.CharField(max_length=200, null=True)

    created = models.DateTimeField(auto_now_add = True, null=True)
    status = models.CharField(max_length=10, null=True, default=False)
    class Meta:
        ordering = ['-created']

class Notification(models.Model):
    user = models.IntegerField(null=True)
    status = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add = True)
    message = models.CharField(max_length=500)
    class Meta:
        ordering = ['-created']
        

class Payments(models.Model):
    user = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user