from django.urls import path
from . import views

urlpatterns = [
    path('experiences_page/<int:user_id>/',views.experiences_page,name='experiences_page')
]