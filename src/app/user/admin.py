from django.contrib import admin

from .models import Company, Section, User

# Register your models here.

@admin.register(Company)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active',) 
    list_filter = ('is_active',) 
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    
    
    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active',) 
    list_filter = ('is_active',) 
    search_fields = ('name',)
    list_display_links = ('id', 'name')    
    
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'company', 'section', 'first_name', 'is_superuser', 'is_staff', 'is_active') 
    list_filter = ('company', 'section', 'is_active') 
    search_fields = ('username', 'first_name')
    list_display_links = ('id', 'username')            