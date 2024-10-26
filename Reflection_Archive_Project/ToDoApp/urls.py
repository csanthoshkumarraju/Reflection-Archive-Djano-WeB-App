from django.urls import path
from . import views

urlpatterns = [
    path('todo_page/<int:user_id>/',views.todo_page,name='todo_page')
]
