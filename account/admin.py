from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "nickname", "email", "phone", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["username", "nickname", "email", "phone"]
    ordering = ["-created_at"]
