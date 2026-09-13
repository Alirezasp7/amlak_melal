from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("phone_number",)}),
    )
    list_display = ("username", "first_name", "last_name", "phone_number", "is_staff")


admin.site.register(User, CustomUserAdmin)