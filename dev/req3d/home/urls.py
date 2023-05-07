from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='home'),
    path('profile', profile, name='profile'),
    path('profile/delete/<int:pk>/', delete_request, name='delete-req'),
    path('profile/object_submit/', update_request, name='object_submit'),
    path('management', card, name='card'),
    path('management/update_admin/', update_admin, name='update_admin'),
    path('management/delete_admin/<int:card_id>', delete_admin, name='delete_admin'),
    path('management/update_card_status/', update_card_status, name='update_card_status'),

]
