from django.urls import path
from . import views

urlpatterns = [
    path('memories_page/<int:user_id>/',views.memories_page,name='memories_page')
]
