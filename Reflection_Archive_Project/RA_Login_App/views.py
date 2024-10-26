# from django.shortcuts import render

# # Create your views here.

# def RA_Login_page(request):
#     return render(request,'RA_Login.html')

from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import RA_LoginForm
from RA_Register_App.models import RA_RegistrationModel

# def RA_Login_page(request): 
#     if request.method == 'POST':
#         form = RA_LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 messages.success(request, 'Login Successful')
#                 # return redirect('RA_homepage', user_id=user.id)
#                 HttpResponse('Login successfull')
#             else:
#                 form.add_error(None, 'Invalid email or password')
#     else:
#         form = RA_LoginForm()

#     return render(request, 'RA_Login.html', {'form': form})

def RA_Login_page(request): 
    if request.method == 'POST':
        form = RA_LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('dashboard',user_id=user.id)  
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = RA_LoginForm()

    return render(request, 'RA_Login.html', {'form': form})

