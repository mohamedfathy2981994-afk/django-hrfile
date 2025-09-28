from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'natid','maindata')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number', 'natid', 'is_active', 'is_staff'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'phone_number', 'natid','maindata')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'natid')
    ordering = ('username',)

# Register the updated admin interface
admin.site.register(CustomUser, CustomUserAdmin)
