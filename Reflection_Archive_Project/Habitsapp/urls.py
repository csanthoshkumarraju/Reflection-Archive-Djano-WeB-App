from django.urls import path
from . import views

urlpatterns = [
    path('habits_page/<int:user_id>/',views.habits_page,name='habits_page')
]