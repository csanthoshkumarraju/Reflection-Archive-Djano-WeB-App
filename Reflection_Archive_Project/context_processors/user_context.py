from RA_Register_App.models import RA_RegistrationModel

def user_context(request):
    user_name = ""
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = RA_RegistrationModel.objects.get(pk=user_id)
            user_name = f"{user.first_name} {user.last_name}"
        except RA_RegistrationModel.DoesNotExist:
            user_name = ""
    
    return {
        'user_name': user_name
    }