from django.urls import path
from . import views

urlpatterns = [
    path('RA_register_page/',views.RA_register_page,name='RA_register_page')
]
