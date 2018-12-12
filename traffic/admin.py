from django.contrib import admin
from .models import Accident
from .models import Population
from .models import RegistrationImage
from .models import CarImage
admin.site.register(Accident)
admin.site.register(Population)
admin.site.register(RegistrationImage)
admin.site.register(CarImage)