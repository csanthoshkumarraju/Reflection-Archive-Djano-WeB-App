from django.contrib import admin
from .models import MemoryModel

class MemoryModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'memory', 'status')

admin.site.register(MemoryModel, MemoryModelAdmin)

