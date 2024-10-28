from django.urls import path
from . import views

urlpatterns = [
    path('tplans_pageodo_page/<int:user_id>/',views.plans_page,name='plans_page')
]