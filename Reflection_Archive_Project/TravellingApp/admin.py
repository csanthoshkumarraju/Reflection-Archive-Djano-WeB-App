from django.contrib import admin
from .models import TravelModel

class TravelModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'destination', 'status')  # List the fields you want to display in the admin list view

admin.site.register(TravelModel, TravelModelAdmin)
