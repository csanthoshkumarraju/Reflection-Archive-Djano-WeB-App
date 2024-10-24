# from django.shortcuts import render

# # Create your views here.

# def RA_reset_pwd_page(request):
#     return render(request,'RA_reset_PWD.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ResetPasswordForm
from RA_Register_App.models import RA_RegistrationModel

def RA_reset_pwd_page(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'RA_reset_PWD.html', {'form': form})

            try:
                user = RA_RegistrationModel.objects.get(email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password has been reset successfully. You can now log in.')
                return redirect('RA_Login_page')
            except RA_RegistrationModel.DoesNotExist:
                form.add_error(None, 'Email address not found.')
                return render(request, 'RA_reset_PWD.html', {'form': form})
    else:
        form = ResetPasswordForm()

    return render(request, 'RA_reset_PWD.html', {'form': form})
