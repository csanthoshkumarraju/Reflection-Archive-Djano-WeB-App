from django.shortcuts import render

# Create your views here.

def RA_Login_page(request):
    return render(request,'RA_Login.html')