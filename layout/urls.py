from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('home/',home,name='layout_home'),
    path('greetings/<str:name>/',greetings,name='layout_greetings'),
    path('newyear/',newyear,name='layout_newyear')
]