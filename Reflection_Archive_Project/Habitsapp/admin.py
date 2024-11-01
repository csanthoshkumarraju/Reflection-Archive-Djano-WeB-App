from django.contrib import admin
from .models import HabitModel

class HabitModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'habit', 'status')  

admin.site.register(HabitModel, HabitModelAdmin)
