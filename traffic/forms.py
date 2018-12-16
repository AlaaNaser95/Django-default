from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from .models import Accident,Profile, CarImage



class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident

        fields=[ "location_longitude", "location_latitude" ]
        widgets = {'location_longitude': forms.HiddenInput(),
        'location_latitude': forms.HiddenInput()}
            


class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields=["accident_image"]
        labels = {
                "accident_image": "Accident Image"
            }


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())