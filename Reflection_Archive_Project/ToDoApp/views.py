from django.shortcuts import render
from RA_Register_App.models import RA_RegistrationModel
# Create your views here.

def todo_page(request,user_id):
    user = RA_RegistrationModel.objects.get(id=user_id)
    if user_id:
        try:
            user = RA_RegistrationModel.objects.get(pk=user_id)
            user_name = f"{user.first_name} {user.last_name}"
        except RA_RegistrationModel.DoesNotExist:
            user_name = ""
    return render(request, 'todo.html', {'user': user,'user_name':user_name})