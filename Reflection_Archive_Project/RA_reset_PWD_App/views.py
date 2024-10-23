from django.shortcuts import render

# Create your views here.

def RA_reset_pwd_page(request):
    return render(request,'RA_reset_PWD.html')