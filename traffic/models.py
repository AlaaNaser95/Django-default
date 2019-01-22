from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    civil_id = models.CharField(max_length=120)
    phone_no= models.CharField(max_length=120,blank=True,null=True)
    email=models.EmailField(max_length=254,blank=True,null=True)

class Accident(models.Model):
    involved_people= models.ManyToManyField(Profile)
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
  
    status=models.CharField(max_length=120,choices=STATUS,default='New')
 
class CarImage(models.Model):
    accident_image=models.ImageField()
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)

class RegistrationImage(models.Model):
    regist_image=models.ImageField()
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)
    
class Involved(models.Model):
    accident=models.ForeignKey(Accident,on_delete=models.CASCADE)
    involved=models.ForeignKey(Profile,on_delete=models.CASCADE)
    STATUS={
    ('No Response','No Response'),
    ('Accepted','Accepted'),
    ('Declined','Declined'),
    }
    comment=models.TextField(default="")
    status=models.CharField(max_length=120,choices=STATUS,default='No Response')

class Report(models.Model):
    detective= models.ForeignKey(User,on_delete=models.CASCADE)
    examiner= models.CharField(max_length=120)
    accident= models.OneToOneField(Accident,on_delete=models.CASCADE)
    comment= models.TextField()
    reported_at= models.DateTimeField(auto_now_add=True)

