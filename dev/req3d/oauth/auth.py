from django.contrib.auth.backends import BaseBackend
from .models import KeycloakUser
from django.contrib.auth.models import User

class KeycloakAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> KeycloakUser:
        print(user['sub'])
        find_user = KeycloakUser.objects.filter(pk=user['sub'])
        if len(find_user) == 0:
            print('User was not found. Saving...')
            new_user = KeycloakUser.objects.create_new_user(user)
            print(new_user)
            return new_user
        print('User was found. Returning...')
        return find_user

    def get_user(self, sub):
        try:
            return KeycloakUser.objects.get(pk=sub)
        except KeycloakUser.DoesNotExist:
            return None