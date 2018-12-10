from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Population(models.Model):
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    civil_id = models.CharField(max_length=120)
    phone_no= models.CharField(max_length=120,blank=True,null=True)
    

class Accident(models.Model):
    involved= models.ManyToManyField(Population)
    location = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    images = models.ImageField()
    STATUS={
    ('Pending','pending'),
    ('Accepted','accepted'),
    ('Expired','expired')
    }
    status=models.CharField(max_length=120,choices=STATUS,default='Pending')