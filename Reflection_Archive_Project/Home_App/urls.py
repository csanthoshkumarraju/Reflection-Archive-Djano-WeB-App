from django.urls import path
from .import views

urlpatterns = [
    path('',views.reflection_archive_home_page,name='reflection_archive_home_page')
]
