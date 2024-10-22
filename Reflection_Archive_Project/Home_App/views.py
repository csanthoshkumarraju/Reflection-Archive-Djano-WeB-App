from django.shortcuts import render

# Create your views here.

def reflection_archive_home_page(request):
    return render(request,'reflection_archive_home.html')