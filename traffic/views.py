from django.shortcuts import render, redirect
from .forms import AccidentForm
from django import forms
from .models import Population,
from django.forms.models import modelform_factory
# Create your views here.
def 
def accidentCreate(request):
        # return redirect('login')
    # followers=[follow.follower.email for follow in Follow.objects.filter(followed=request.user)]
    form=AccidentForm()
    involvedForm=modelform_factory(Population,form=forms.ModelForm, fields=('civil_id',))
    regist_images_form=modelform_factory(RegistrationImage,form=forms.ModelForm, fields=('regist_image1','regist_image2','regist_image3','regist_image4',))
    car_images_form=modelform_factory(CarImage,form=forms.ModelForm, fields=('car_image1','car_image2','car_image3','car_image4',))

    if request.method == "POST":
        form = AccidentForm(request.POST, request.FILES)
        if form.is_valid():
            accident=form.save()
            myPopulation=Population.objects.get(id=request.user.id)
            p, created = Population.objects.get_or_create(civil_id=request.POST['civil_id'])
            accident.involved.add(myPopulation,p)
            accident.save()
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
    return render(request, "test.html", context )


def accidentCreate(request):
        # return redirect('login')
    # followers=[follow.follower.email for follow in Follow.objects.filter(followed=request.user)]
    form=AccidentForm()
    involvedForm=modelform_factory(Population,form=forms.ModelForm, fields=('civil_id',))
    regist_img_Form=modelform_factory(CarImage,form=forms.ModelForm, fields=('image',))
    if request.method == "POST":
        form = AccidentForm(request.POST, request.FILES)
        if form.is_valid():
            accident=form.save()
            myPopulation=Population.objects.get(id=request.user.id)
            p, created = Population.objects.get_or_create(civil_id=request.POST['civil_id'])
            accident.involved.add(myPopulation,p)
            accident.save()
            # sendemail(request.user,followers)
            # messages.success(request, "Successfully Created!")
            return redirect('create-accident')
        print (form.errors)

    context={
        "involvedForm":involvedForm,
        "form":form,

    }
    return render(request, "test.html", context )