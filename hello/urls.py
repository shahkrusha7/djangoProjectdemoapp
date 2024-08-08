from django.contrib import admin
from django.urls import path

from hello import views

urlpatterns = [
    path('hello/',views.hello,name='hello'),
    path('home/',views.home,name='home')
]