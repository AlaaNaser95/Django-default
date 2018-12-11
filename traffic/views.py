from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sazidahossain@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
