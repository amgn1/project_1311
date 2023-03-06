from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', appform_view, name='appform'),
]
