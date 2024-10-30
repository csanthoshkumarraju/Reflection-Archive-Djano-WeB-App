from django.urls import path
from . import views

urlpatterns = [
    path('travel_page/<int:user_id>/', views.travel_page, name='travel_page')  
]
