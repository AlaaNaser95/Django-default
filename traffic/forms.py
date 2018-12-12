from django import forms
from django.contrib.auth.models import User
from .models import Accident


class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields=["location"]


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
#         widgets={
#             'date': forms.DateInput(attrs={'type':"date"}),
#             'time': forms.TimeInput(attrs={'type':"time"}),
#         }


# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Pizza

#     # Representing the many to many related field in Pizza
#     users = forms.ModelMultipleChoiceField(queryset=User.objects.all())

#     # Overriding __init__ here allows us to provide initial
#     # data for 'toppings' field
#     # def __init__(self, *args, **kwargs):
#     #     # Only in case we build the form from an instance
#     #     # (otherwise, 'toppings' list should be empty)
#     #     if kwargs.get('instance'):
#     #         # We get the 'initial' keyword argument or initialize it
#     #         # as a dict if it didn't exist.                
#     #         initial = kwargs.setdefault('initial', {})
#     #         # The widget for a ModelMultipleChoiceField expects
#     #         # a list of primary key for the selected data.
#     #         initial['toppings'] = [t.pk for t in kwargs['instance'].topping_set.all()]

#     #     forms.ModelForm.__init__(self, *args, **kwargs)

#     # Overriding save allows us to process the value of 'toppings' field    
#     def save(self, commit=True):
#         # Get the unsave Pizza instance
#         instance = forms.ModelForm.save(self, False)

#         # Prepare a 'save_m2m' method for the form,
#         old_save_m2m = self.save_m2m
#         def save_m2m():
#            old_save_m2m()
#            # This is where we actually link the pizza with toppings
#            instance.users_set.clear()
#            instance.users_set.add(*self.cleaned_data['users'])
#         self.save_m2m = save_m2m

#         # Do we need to save all changes now?
#         if commit:
#             instance.save()
#             self.save_m2m()

#         return instance