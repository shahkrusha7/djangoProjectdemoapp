import datetime

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'layout/home.html')

def greetings(request,name):
    return render(request, 'layout/greetings.html',{'username':name})

def newyear(request):
    date=datetime.datetime.utcnow()
    return render(request, 'layout/newyear.html',
                  {'newyear':date.month==1 and date.day==1})