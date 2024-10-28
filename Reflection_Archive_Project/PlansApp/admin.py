from django.contrib import admin
from .models import plan_model

@admin.register(plan_model)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status')
    search_fields = ('plan',)

