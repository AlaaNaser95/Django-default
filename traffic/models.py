from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Population(models.Model):
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    civil_id = models.CharField(max_length=120)
    phone_no= models.CharField(max_length=120,blank=True,null=True)
@receiver(post_save, sender=User)
def create_user_population(sender, instance, created, **kwargs):
    if created:
        Population.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_population(sender, instance, **kwargs):
    instance.population.save()

class Accident(models.Model):
    involved= models.ManyToManyField(Population)
    location = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    STATUS={
    ('Pending','pending'),
    ('Accepted','accepted'),
    ('Expired','expired')
    }
    status=models.CharField(max_length=120,choices=STATUS,default='Pending')

class RegistrationImage(models.model):
    regist_image1=models.ImageField()
    regist_image2=models.ImageField(blank=True,null=True)
    regist_image3=models.ImageField(blank=True,null=True)
    regist_image4=models.ImageField(blank=True,null=True)
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)

class CarImage(models.model):
    car_image1=models.ImageField()
    car_image2=models.ImageField()
    accident=models.ForeignKey(Accident, on_delete=models.CASCADE)