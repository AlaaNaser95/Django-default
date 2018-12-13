from django.shortcuts import render, redirect
from .forms import AccidentForm, UserRegister, UserLogin 
from django import forms
from .models import Population, RegistrationImage,CarImage,Accident
from django.forms.models import modelform_factory
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.forms import modelformset_factory
# Create your views here.

def accidentCreate(request):
    GroupInvolvedFormSet = modelformset_factory(
            Population,
            form = forms.ModelForm,
            fields=('civil_id',),
            labels={'civil_id':'The other civil id'},
            extra = 3
        )
    GroupRegistrationImageFormSet = modelformset_factory(
            RegistrationImage,
            form = forms.ModelForm,
            fields=('regist_image',),
            labels={'regist_image':'Car registration Image'},
            extra = 2
        )
    formset = GroupInvolvedFormSet(queryset=Population.objects.none())
    registrationFormset = GroupRegistrationImageFormSet(queryset=RegistrationImage.objects.none())
    form=AccidentForm()
    car_images_form=modelform_factory(CarImage,form=forms.ModelForm, fields=('accident_image',))
    
    if request.method == "POST":
        form = AccidentForm(request.POST, request.FILES)
        formset = GroupInvolvedFormSet(request.POST, queryset=Population.objects.none())
        registrationFormset=GroupRegistrationImageFormSet(
                request.POST,
                request.FILES,
                queryset=RegistrationImage.objects.none(),
            )

        if form.is_valid() and formset.is_valid() and registrationFormset.is_valid():
            accident=form.save()
            myPopulation=Population.objects.get(user_id=request.user.id)
            accident.involved.add(myPopulation)

            for x in formset:
                if x.cleaned_data:
                    pop=x.save(commit=False)
                    p, created = Population.objects.get_or_create(civil_id=pop.civil_id)
                    accident.involved.add(p)

            for x in registrationFormset:
                if x.cleaned_data:
                    regist_images=x.save(commit=False)
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
    context={
        "formset":formset,
        "form":form,
        "registrationFormset":registrationFormset,
        "car_images_form":car_images_form,

    }
    return render(request, "accident.html", context )

def user_register(request):
    form = UserRegister()
    popForm=modelform_factory(Population, form=forms.ModelForm,fields=('civil_id','phone_no'),labels={'civil_id':'Civil id', 'phone_no':'Mobile Number'})
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


def user_profile(request,profile_id):
    profile=Population.objects.get(id=profile_id)
    context = {
        "profile":profile
    }
    return render(request, 'profile.html', context)


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


def accidentList(request):
    myPopulation=Population.objects.get(user_id=request.user.id)
    accidents=Accident.objects.filter(involved=myPopulation)
    # previous_books=chain(previous_books, Book.objects.filter(booker=request.user, event__date=datetime.date.today(), event__time__lt=datetime.datetime.now()))
    # upcoming_events = {upcoming_book.event for upcoming_book in upcoming_books}
    # tickets=sum(upcoming_books.values_list('tickets', flat=True))

    # previous_events = previous_events.values_list("event",falt=True).distinct()
    # upcoming_events = {upcoming_book.event for upcoming_book in upcoming_books}

    # previous_events={previous_book.event for previous_book in Book.objects.filter(booker=request.user, event__date__lte=timezone.now(), event__time__lte=timezone.now())}
    # upcoming_books=Book.objects.filter(booker=request.user, event__date__gte=timezone.now(), event__time__gte=timezone.now())
    
    
    context={
        'accidents':accidents,  
    }

    return render(request, "accidentList.html",context)

def accidentDetail(request, accident_id):
    accident = Accident.objects.get(id=accident_id)
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