from django.shortcuts import render, redirect
from .forms import AccidentForm, UserRegister, UserLogin 
from django import forms
from .models import Population
from django.forms.models import modelform_factory
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.


def accidentCreate(request):
        # return redirect('login')
    # followers=[follow.follower.email for follow in Follow.objects.filter(followed=request.user)]
    form=AccidentForm()
    involvedForm=modelform_factory(Population,form=forms.ModelForm, fields=('civil_id',))
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

            return redirect('successfully_login')
        print (form.errors)

    context={
        "involvedForm":involvedForm,
        "form":form,

    }
    return render(request, "accident.html", context )



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
                return redirect('successfully_login')

    context = {
        "form":form
    }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    # Where you would like to redirect the user after successfully logging out
    return redirect("successful-logout")




































































