from django.shortcuts import render

# Create your views here.

def RA_register_page(request):
    return render(request,'RA_register.html')