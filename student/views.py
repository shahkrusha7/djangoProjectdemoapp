from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'student/home.html')

def aboutus(request):
    return render(request, 'student/aboutus.html')

def dashboard(request):
    return render(request, 'student/dashboard.html')