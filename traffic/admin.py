from django.contrib import admin

# Register your models here.
from .models import Accident
from .models import Population
admin.site.register(Accident)
admin.site.register(Population)