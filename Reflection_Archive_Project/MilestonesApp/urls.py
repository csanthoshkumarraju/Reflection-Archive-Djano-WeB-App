from django.urls import path
from . import views

urlpatterns = [
    path('milestones_page/<int:user_id>/',views.milestones_page,name='milestones_page')
]