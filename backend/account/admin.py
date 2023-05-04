from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AdminChangeForm
from .models import User, Profile
# Register your models here.

# User = get_user_model()

class UserAdmin(BaseUserAdmin):
    model = User
    search_fields = ['name', 'email', 'department']
    ordering = ['created']
    list_display = ['name']
    list_filter = ['is_superuser']

    form = AdminChangeForm

    fieldsets = (
        (None, {'fields': (['email'])}),
        ('Personal info', {'fields': ('name', 'department', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('name', 'email', 'department','password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
