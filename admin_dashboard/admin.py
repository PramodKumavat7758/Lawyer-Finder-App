
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from lawyer.models import Lawyer, Blog

from .models import CustomUser




@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile', 'is_approved')
    list_filter = ('is_approved', 'specializations')
    search_fields = ('full_name', 'email', 'mobile')
    actions = ['approve_lawyer']

    def approve_lawyer(self, request, queryset):
        queryset.update(is_approved=True)
    approve_lawyer.short_description = "Approve selected lawyers"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'id')
    search_fields = ('title', 'author__full_name')

# Extend User Admin to include update and delete
#dash.site.unregister(User)  # Unregister default User dash
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
