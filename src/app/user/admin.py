from django.contrib import admin
from .models import User, Company, Section

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'company', 'section', 'date_joined', 'last_login')
    list_display_links = ('id', 'username')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'company', 'section')
    
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    list_filter = ('is_active',)
    
    
    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    list_filter = ('is_active',)    