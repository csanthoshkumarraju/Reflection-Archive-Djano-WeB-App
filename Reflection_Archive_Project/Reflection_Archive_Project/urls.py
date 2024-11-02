"""
URL configuration for Reflection_Archive_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home_App.urls')),
    path('',include('RA_Register_App.urls')),
    path('',include('RA_Login_App.urls')),
    path('',include('RA_reset_PWD_App.urls')),
    path('',include('dashboardapp.urls')),
    path('',include('ToDoApp.urls')),
    path('',include('PlansApp.urls')),
    path('',include('AchievementApp.urls')),
    path('',include('TravellingApp.urls')),
    path('',include('ExeperienceApp.urls')),
    path('',include('Habitsapp.urls')),
    path('',include('MemoriesApp.urls')),
    path('',include('LifegoalsApp.urls')),
    path('',include('MilestonesApp.urls')),

]
