from django.contrib import admin

from .models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "password",
        "is_staff",
        "is_active",
        "is_superuser",
        "last_login",
        "first_name",
        "last_name",
        "phone_number",
        "date_joined",
        "avatar",
        "city",
    )
    list_filter = (
        "username",
        "is_active",
        "is_superuser",
    )
    search_fields = ("first_name", "last_name")
