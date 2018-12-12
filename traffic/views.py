from django.shortcuts import render, redirect
from .forms import AccidentForm, UserRegister, UserLogin 
from django import forms
from .models import Population, RegistrationImage,CarImage
from django.forms.models import modelform_factory
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def accidentCreate(request):
        # return redirect('login')
    # followers=[follow.follower.email for follow in Follow.objects.filter(followed=request.user)]
    form=AccidentForm()
    involvedForm=modelform_factory(Population,form=forms.ModelForm, fields=('civil_id',))
    regist_images_form=modelform_factory(RegistrationImage,form=forms.ModelForm, fields=('regist_image1','regist_image2',))
    car_images_form=modelform_factory(CarImage,form=forms.ModelForm, fields=('car_image1','car_image2','car_image3','car_image4',))

    if request.method == "POST":
        form = AccidentForm(request.POST, request.FILES)
        if form.is_valid():
            accident=form.save()
            myPopulation=Population.objects.get(user_id=request.user.id)
            p, created = Population.objects.get_or_create(civil_id=request.POST['civil_id'])
            accident.involved.add(myPopulation,p)
            regist_images_form=regist_images_form(request.POST,request.FILES)
            regist_images=regist_images_form.save(commit=False)
            regist_images.accident=accident
            regist_images.save()
            car_images_form=car_images_form(request.POST,request.FILES)
            car_images=car_images_form.save(commit=False)
            car_images.accident=accident
            car_images.save()
            regist_images=accident.save()
            # sendemail(request.user,followers)
            # messages.success(request, "Successfully Created!")
            return redirect('create-accident')
        print (form.errors)

    context={
        "involvedForm":involvedForm,
        "form":form,
        "regist_images_form":regist_images_form,
        "car_images_form":car_images_form,

    }
    return render(request, "accident.html", context )


# def accidentCreate(request):
#         # return redirect('login')
#     # followers=[follow.follower.email for follow in Follow.objects.filter(followed=request.user)]
#     form=AccidentForm()
#     involvedForm=modelform_factory(Population,form=forms.ModelForm, fields=('civil_id',))
#     regist_img_Form=modelform_factory(CarImage,form=forms.ModelForm, fields=('image',))
#     if request.method == "POST":
#         form = AccidentForm(request.POST, request.FILES)
#         if form.is_valid():
#             accident=form.save()
#             myPopulation=Population.objects.get(id=request.user.id)
#             p, created = Population.objects.get_or_create(civil_id=request.POST['civil_id'])
#             accident.involved.add(myPopulation,p)
#             accident.save()

#             # sendemail(request.user,followers)
#             # messages.success(request, "Successfully Created!")

#             return redirect('successfully_login')
#         print (form.errors)

#     context={
#         "involvedForm":involvedForm,
#         "form":form,

#     }
#     return render(request, "accident.html", context )



def user_register(request):
    form = UserRegister()
    popForm=modelform_factory(Population, form=forms.ModelForm,fields=('civil_id',))
    if request.method == 'POST':
        form = UserRegister(request.POST)
        popForm=popForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            pop=popForm.save(commit=False)
            pop.user=user
            pop.save()
            login(request, user)
            # Where you want to go after a successful signup
            return redirect('create-accident')
    context = {
        "form":form,
        "popForm":popForm,
    }
    return render(request, 'register.html', context)



def user_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect('create-accident')

    context = {
        "form":form
    }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    # Where you would like to redirect the user after successfully logging out
    return redirect("successful-logout")


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sazidahossain@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )    

