from django.urls import path
from . import views

urlpatterns = [
    path('RA_Login_page/',views.RA_Login_page,name='RA_Login_page')
]
