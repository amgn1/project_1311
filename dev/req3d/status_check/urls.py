from django.urls import path
from . import views

urlpatterns = [
    path('', views.status_check, name='status_check'),
]