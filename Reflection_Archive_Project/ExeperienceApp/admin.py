from django.contrib import admin
from .models import ExperienceModel

class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'experience', 'status')  

admin.site.register(ExperienceModel, ExperienceModelAdmin)

