from django.shortcuts import render, redirect
from .forms import AccidentForm, UserRegister, UserLogin, CarImageForm 
from django import forms
from .models import Profile, RegistrationImage,CarImage,Accident
from django.forms.models import modelform_factory
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.forms import modelformset_factory
from django.contrib import messages
# Create your views here.

def home(request):
    
    return render(request, 'home.html')


def accidentCreate(request):
    if request.user.is_anonymous:
        return redirect('login')
    GroupInvolvedFormSet = modelformset_factory(
            Profile,
            form = forms.ModelForm,
            fields=('civil_id',),
            labels={'civil_id':'The other civil id'},
            extra = 1

        )
    GroupRegistrationImageFormSet = modelformset_factory(
            RegistrationImage,
            form = forms.ModelForm,
            fields=('regist_image',),
            labels={'regist_image':'Involved Car registration'},
            extra = 2
        )
    involvedFormset = GroupInvolvedFormSet(queryset=Profile.objects.none())
    registrationFormset = GroupRegistrationImageFormSet(queryset=RegistrationImage.objects.none())
    accidentForm=AccidentForm()
    car_images_form=CarImageForm()
    # car_images_form=modelform_factory(CarImage,form=forms.ModelForm, fields=('accident_image',))
    """In case Of Post"""
    # files = request.FILES.getlist('file_field')
    # print(files)
    if request.method == "POST":

        accidentForm = AccidentForm(request.POST, request.FILES)
        involvedFormset = GroupInvolvedFormSet(request.POST, queryset=Profile.objects.none())
        registrationFormset=GroupRegistrationImageFormSet(
                request.POST,
                request.FILES,
                queryset=RegistrationImage.objects.none(),
            )
        car_images_form=CarImageForm(request.POST,request.FILES)

        if accidentForm.is_valid() and involvedFormset.is_valid() and registrationFormset.is_valid() and car_images_form.is_valid():
            accident=accidentForm.save()
            myProfile=Profile.objects.get(user_id=request.user.id)
            accident.involved.add(myProfile)

            for x in involvedFormset:
                if x.cleaned_data:
                    pop=x.save(commit=False)
                    p, created = Profile.objects.get_or_create(civil_id=pop.civil_id)
                    accident.involved.add(p)

            for x in registrationFormset:
                if x.cleaned_data:
                    regist_images=x.save(commit=False)
                    regist_images.accident=accident
                    regist_images.save()
            files = request.FILES.getlist('file_field')
            for file in files:
                car_images=CarImage.objects.create(accident_image=file,accident=accident)
                car_images.save()
            regist_images=accident.save()
            # sendemail(request.user,followers)
            messages.success(request, "Successfully Submitted!")
            return redirect('home')
    context={
        "involvedFormset":involvedFormset,
        "accidentForm":accidentForm,
        "registrationFormset":registrationFormset,
        "car_images_form":car_images_form,

    }
    return render(request, "accident.html", context )

def user_register(request):
    form = UserRegister()
    popForm=modelform_factory(Profile, form=forms.ModelForm,fields=('civil_id','phone_no'),labels={'civil_id':'Civil id', 'phone_no':'Mobile Number'})
    if request.method == 'POST':
        form = UserRegister(request.POST)
        popForm=popForm(request.POST)
        if form.is_valid() and popForm.is_valid():
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


def user_profile(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'profile.html')


def updateProfile(request):
    if request.user.is_anonymous:
        return redirect('login')
    profile=request.user.profile
    prof_form = modelform_factory(Profile, form=forms.ModelForm,fields=('phone_no',),labels={'phone_no':'Mobile Number'})
    user_form = modelform_factory(User, form=UserRegister,fields=('username','password','email',))
    user_form = user_form(instance=profile.user)
    prof_form = prof_form(instance=profile)
    if request.method == "POST":
        prof_form = modelform_factory(Profile, form=forms.ModelForm,fields=('phone_no',),labels={'phone_no':'Mobile Number'})
        user_form = modelform_factory(User, form=UserRegister,fields=('username','password','email',))
        prof_form = prof_form(request.POST,instance=profile)
        user_form = user_form(request.POST,instance=request.user)
        if prof_form.is_valid() and user_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            prof_form.save()
            # login(request.user)
            # messages.success(request, "Successfully Updated!")
            return redirect('create-accident')    
    
    context = {
        "prof_form":prof_form,
        "user_form":user_form,
        
        }
    return render(request, 'updateProfile.html', context)


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
    return redirect("home")


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sazidahossain@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )    


def accidentList(request):
    if request.user.is_anonymous:
        return redirect('login')
    myProfile=Profile.objects.get(user=request.user)
    accidents=Accident.objects.filter(involved=myProfile)
    context={
        'accidents':accidents,  
    }

    return render(request, "accidentList.html",context)

def accidentDetail(request, accident_id):
    if request.user.is_anonymous:
        return redirect('login')
    accident = Accident.objects.get(id=accident_id)
    #need to check if the user involved in the accident
    
    car_images=CarImage.objects.filter(accident=accident)
    regis_images=RegistrationImage.objects.filter(accident=accident)
    # student=classroom.student_set.all().order_by('name','-exam_grade')
            # messages.success(request, "Successfully booked!")
    context = {
        "accident": accident,
        "car_images":car_images,
        "regis_images":regis_images
        }
    return render(request, 'accidentDetail.html', context)