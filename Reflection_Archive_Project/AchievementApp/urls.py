from django.urls import path
from . import views

urlpatterns = [
    path('achievements_page/<int:user_id>/',views.achievements_page,name='achievements_page')
]
