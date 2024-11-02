from django.contrib import admin
from .models import MilestoneModel

class MilestoneModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'milestone', 'date_added')  

admin.site.register(MilestoneModel, MilestoneModelAdmin)
