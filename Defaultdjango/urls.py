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
from traffic.views import accidentCreate, user_login, user_register, email, accidentList,accidentDetail,user_profile,updateProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accident/form/', accidentCreate,name='create-accident'),
    path('login/', user_login,name='login'),
    path('register/', user_register,name='register'),

    path('sendMail/', email),
    path('accident/list/', accidentList,name='accident-list'),
    path('accident/detail/<int:accident_id>/', accidentDetail,name='accident-detail'),
    path('profile/<int:profile_id>/', user_profile,name='profile'),
    path('profile/update/<int:profile_id>/', updateProfile,name='update-profile'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)