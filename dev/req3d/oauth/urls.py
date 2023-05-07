from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('login', keycloak_login, name='oauth_login'),
    path('login/redirect', keycloak_login_redirect, name='discord_login_redirect'),
    path('logout', keycloak_logout, name='oauth_logout')
]


