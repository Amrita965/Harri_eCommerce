from django.contrib import admin
from .models import UserInfo

# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "address", "password_reset_code", "reset_code_created_at", "created_at", "updated_at")
    search_fields = ("id", "phone", "address")