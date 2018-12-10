from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Accident(models.Model):
    user= models.ForeignKey(User, default=1,  related_name='addresses', on_delete=models.CASCADE)
    location = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    images = models.CharField(max_length=120)
    status=models.CharField(max_length=120)

class Population(models.Model):
    civil_id = models.CharField(max_length=120)
    name = models.TextField()
    phone_no= models.TextField()
    
