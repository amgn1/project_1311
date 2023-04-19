from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import DiscordUser

class DiscordUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    list_display = ('discord_tag', 'last_login', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Personal info', {
            'fields': ('discord_tag', 'last_login')
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_active')
        }),
    )
    readonly_fields = ('discord_tag', 'last_login')
    search_fields = ('discord_tag',)
    ordering = ('discord_tag',)
    filter_horizontal = ()

admin.site.register(DiscordUser, DiscordUserAdmin)
admin.site.unregister(Group)
