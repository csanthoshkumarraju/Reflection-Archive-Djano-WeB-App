from django.urls import path
from . import views

urlpatterns = [
    path('goals_page/<int:user_id>/',views.goals_page,name='goals_page')
]