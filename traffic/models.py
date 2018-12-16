from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    civil_id = models.CharField(max_length=120,unique=True,error_messages={'unique':"This civil id has already been used."})
    phone_no= models.CharField(max_length=120,blank=True,null=True)






# @receiver(post_save, sender=User)

# def create_user_population(sender, instance, created, **kwargs):
#     if created:
#         Population.objects.create(user=instance)



# @receiver(post_save, sender=User)

# def save_user_population(sender, instance, **kwargs):
#     instance.population.save()

    

class Accident(models.Model):
    involved= models.ManyToManyField(Profile)
    location_longitude = models.DecimalField(max_digits=9, default=1, decimal_places=6)
    location_latitude = models.DecimalField(max_digits=9, default=1,decimal_places=6)
    date_time = models.DateTimeField(auto_now_add=True)
    STATUS={
    ('Pending','pending'),
    ('Accepted','accepted'),
    ('Expired','expired')
    }
    status=models.CharField(max_length=120,choices=STATUS,default='Pending')

class CarImage(models.Model):
    accident_image=models.FileField()
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)

class RegistrationImage(models.Model):
    regist_image=models.ImageField()
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)