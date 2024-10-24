from django.contrib import admin
from .models import RA_RegistrationModel

class RARegistrationAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(RA_RegistrationModel, RARegistrationAdmin)


