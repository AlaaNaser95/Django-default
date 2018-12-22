"""Defaultdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from traffic.views import accidentCreate, user_login, user_register, email, accidentList,accidentDetail,user_profile, home, user_logout,updateProfile,accidentListStaff,accidentDetailStaff,reportStaff,compliance,declined,send_pdf,trial




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accident/form/', accidentCreate,name='create-accident'),
    path('login/', user_login,name='login'),
    path('register/', user_register,name='register'),
    path('home/', home,name='home'),
    path('logout/', user_logout ,name='logout'),
    path('sendMail/', email),
    path('accident/list/', accidentList,name='accident-list'),
    path('accident/detail/<int:accident_id>/', accidentDetail,name='accident-detail'),
    path('profile/', user_profile,name='profile'),
    path('profile/update/', updateProfile,name='update-profile'),


    path('staff/accident/list', accidentListStaff,name='staff-accident-list'),
    path('staff/accident/detail/<int:accident_id>/', accidentDetailStaff,name='staff-accident-detail'),
    path('staff/accident/report/<int:accident_id>/', reportStaff ,name='report'),

    path('accident/compliance/<int:accident_id>/', compliance,name='accident-compliance'),
    path('accident/decline/<int:accident_id>/', declined,name='accident-decline'),
    path('sendPdf/', send_pdf,name='accident-pdf'),
    path('trial/', trial,name='accident-trial')
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)