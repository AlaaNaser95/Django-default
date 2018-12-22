from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from .models import Accident,Profile, CarImage,Report



class AccidentForm(forms.ModelForm):

    class Meta:
        model = Accident
        fields=[ "location_longitude", "location_latitude" ]
        widgets = {'location_longitude': forms.HiddenInput(),
        'location_latitude': forms.HiddenInput()}
            


class CarImageForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = CarImage
        fields=['file_field']
        labels = {
                "file_field": "Accident Image"
            }


class UserRegister(forms.ModelForm):
    first_name=forms.CharField(max_length=30,required=True)
    last_name=forms.CharField(max_length=150,required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['civil_id', 'phone_no']

class ProfileAccidentForm(forms.ModelForm):
    email=forms.EmailField(max_length=254, required=True)
    class Meta:
        model = Profile
        fields = ['civil_id', 'email']
    # def clean(self):
    #     cleaned_data = super(ProfileForm, self).clean()
    #     # additional cleaning here
    #     return cleaned_data

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['examiner','comment']
