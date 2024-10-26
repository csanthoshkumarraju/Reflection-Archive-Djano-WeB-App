from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<int:user_id>/',views.dashboard,name='dashboard')
]
