from django.contrib import admin
from django.urls import path

from student import views

urlpatterns = [
    path('home/',views.home,name='student_home'),
    path('aboutus/',views.aboutus,name='student_aboutus'),
    path('dashboard/',views.dashboard,name='student_dashboard')
]