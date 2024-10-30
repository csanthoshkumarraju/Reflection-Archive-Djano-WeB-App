from django.contrib import admin
from .models import acheivements_model
# Register your models here.

class AcheivementsModelAdmin(admin.ModelAdmin):
    list_display = ('user','id','acheiement','achievment_status')

admin.site.register(acheivements_model,AcheivementsModelAdmin)
