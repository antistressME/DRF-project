from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ("password",)
    list_filter = (
        "email",
        "phone_number",
        "city",
    )
