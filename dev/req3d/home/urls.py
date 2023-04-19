from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='home'),
    path('profile', profile, name='profile'),
    path('profile/delete/<int:pk>/', delete_request, name='delete-req'),
    path('profile/object_submit/', update_request, name='object_submit'),
   
]
