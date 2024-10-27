from django.contrib import admin
from .models import todo_model

class TodoModelAdmin(admin.ModelAdmin):
    list_display = ('user','id', 'todo', 'status')  # List the fields you want to display in the admin list view

admin.site.register(todo_model, TodoModelAdmin)

