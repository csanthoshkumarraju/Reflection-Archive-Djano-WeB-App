from django.contrib import admin
from .models import GoalModel  

@admin.register(GoalModel)  
class GoalAdmin(admin.ModelAdmin):  
    list_display = ('user', 'goal', 'status')  
    search_fields = ('goal',)  
