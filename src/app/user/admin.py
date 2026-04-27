from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.user.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):    
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('department', 'phone', 'deleted_at')}),
    )
