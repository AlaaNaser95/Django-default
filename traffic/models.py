from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Accident(models.Model):
    user= models.ManyToManyField(User)
    location = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    images = models.ImageField()
    STATUS={
    ('Pending','pending'),
    ('Accepted','accepted'),
    ('Expired','expired')
    }
    status=models.CharField(max_length=120,choices=STATUS)

class Population(models.Model):
    civil_id = models.CharField(max_length=120)
    name = models.TextField()
    phone_no= models.TextField()
    
