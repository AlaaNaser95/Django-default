from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import validate_file_extension

class Profile(models.Model):
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    civil_id = models.CharField(max_length=120)
    phone_no= models.CharField(max_length=120,blank=True,null=True)
    email=models.EmailField(max_length=254,blank=True,null=True)

class Accident(models.Model):
    involved= models.ManyToManyField(Profile)
    location_longitude = models.DecimalField(max_digits=9, default=1, decimal_places=6)
    location_latitude = models.DecimalField(max_digits=9, default=1,decimal_places=6)
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="")
    STATUS={
    ('New','new'),
    ('Pending','pending'),
    ('Accepted','accepted'),
    ('Expired','expired'),
    
    }
    STATUS_FOR_STAFF={
    ('Accepted','accepted'),
    ('Declined','declined'),
    }
    status=models.CharField(max_length=120,choices=STATUS,default='New')
    status_for_staff=models.CharField(max_length=120,blank=True,null=True,choices=STATUS_FOR_STAFF)

class CarImage(models.Model):
    accident_image=models.FileField(validators=[validate_file_extension])
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)

class RegistrationImage(models.Model):
    regist_image=models.ImageField()
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)


class Report(models.Model):
    detective= models.ForeignKey(User,on_delete=models.CASCADE)
    examiner= models.CharField(max_length=120)
    accident= models.OneToOneField(Accident,on_delete=models.CASCADE)
    comment= models.TextField()
    reported_at= models.DateTimeField(auto_now_add=True)

