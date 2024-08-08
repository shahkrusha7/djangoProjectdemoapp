from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello , Welcome to our hello app!</h1>")

def home(request):
    return HttpResponse("<h3>Home page of hello app</h3>")