from django import forms
from django.contrib.auth.models import User
from .models import Accident


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude=['creator']

        widgets={
            'date': forms.DateInput(attrs={'type':"date"}),
            'time': forms.TimeInput(attrs={'type':"time"}),
        }