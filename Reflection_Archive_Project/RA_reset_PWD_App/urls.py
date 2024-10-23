from django.urls import path
from . import views

urlpatterns = [
    path('RA_reset_pwd_page/',views.RA_reset_pwd_page,name='RA_reset_pwd_page')
]
