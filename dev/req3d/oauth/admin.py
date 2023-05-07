from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import KeycloakUser

class KeycloakUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    list_display = ('full_name', 'last_login', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Personal info', {
            'fields': ('full_name', 'last_login')
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_active')
        }),
    )
    readonly_fields = ('full_name', 'last_login')
    search_fields = ('full_name',)
    ordering = ('full_name',)
    filter_horizontal = ()

admin.site.register(KeycloakUser, KeycloakUserAdmin)
admin.site.unregister(Group)
