from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('home/',home,name='task_home'),
    path('addtask/',addtask,name='addtask')
]