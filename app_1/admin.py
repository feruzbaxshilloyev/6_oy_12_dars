from django.contrib import admin
from .models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_info', 'image', 'description', 'created_at', 'updated_at')
