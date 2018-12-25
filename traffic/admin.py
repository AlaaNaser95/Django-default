from django.contrib import admin
from .models import Accident,Profile,RegistrationImage,CarImage,Report,Involved

admin.site.register(Accident)
admin.site.register(Profile)
admin.site.register(RegistrationImage)
admin.site.register(CarImage)
admin.site.register(Report)
admin.site.register(Involved)