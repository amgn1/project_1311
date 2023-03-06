from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('appform/', appform_view, name='appform'),
    path('add/', add_data, name='add_data'),
    path('suc/', success, name='success')
   
]
