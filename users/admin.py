from django.contrib import admin

from products.admin import Bascet_admin

from .models import Email_Verification, User


@admin.register(User)
class User_admin(admin.ModelAdmin):
    list_display = ['username']
    inlines = [Bascet_admin]

@admin.register(Email_Verification)
class Email_Verification_Admin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    fields = ['code', 'user', 'created_at', 'expiration']
    readonly_fields = ['created_at']