from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RA_registrationForm
from .models import RA_RegistrationModel


def RA_register_page(request):
    if request.method == 'POST':
        form = RA_registrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = RA_RegistrationModel(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)  # Hash the password
            user.save()
            messages.success(request, "Registration successful")
            return redirect('RA_Login_page')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RA_registrationForm()

    return render(request, 'RA_register.html', {'form': form})


