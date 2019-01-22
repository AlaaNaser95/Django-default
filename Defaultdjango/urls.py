
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


<<<<<<< HEAD
from traffic.views import (accidentCreate, user_login, user_register, email, accidentList,accidentDetail,user_profile, home, user_logout,updateProfile,accidentListStaff,accidentDetailStaff,compliance,declined,report,send_pdf,trial,involved)
=======
from traffic.views import accidentCreate, user_login, user_register, email, accidentList,accidentDetail,user_profile, home, user_logout,updateProfile,accidentListStaff,accidentDetailStaff,compliance,declined,report,send_pdf,involved

>>>>>>> e4c7b9b30aca467a10a7c9007b6356231f55652d




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accident/form/<int:involved>/', accidentCreate,name='create-accident'),
    path('login/', user_login,name='login'),
    path('register/', user_register,name='register'),
    path('home/', home,name='home'),
    path('logout/', user_logout ,name='logout'),
    path('sendMail/', email),
    path('accident/list/', accidentList,name='accident-list'),
    path('accident/detail/<int:accident_id>/', accidentDetail,name='accident-detail'),
    path('profile/', user_profile,name='profile'),
    path('report/', report,name='accident-report'),
    path('profile/update/', updateProfile,name='update-profile'),
    path('report/', report,name='accident-report'),
    path('accident/involved/', involved,name='involved'),


    path('staff/accident/list', accidentListStaff,name='staff-accident-list'),
    path('staff/accident/detail/<int:accident_id>/', accidentDetailStaff,name='staff-accident-detail'),


    path('accident/compliance/<int:accident_id>/<int:involved_id>/', compliance,name='accident-compliance'),
    path('accident/decline/<int:accident_id>/<int:involved_id>/', declined,name='accident-decline'),
    path('sendPdf/', send_pdf,name='accident-pdf'),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)