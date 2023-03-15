from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('login', discord_login, name='oauth_login'),
    path('login/redirect', discord_login_redirect, name='discord_login_redirect'),
    path('logout', discord_logout, name='oauth_logout')
]


