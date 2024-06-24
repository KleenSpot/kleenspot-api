from django.contrib import admin
from .models.models import  CustomUser, AccessToken, LoginHistory

   
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'last_logout_time', 'inactive_duration')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active', 'date_joined')

@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at', 'expired_at')
    search_fields = ('user__username', 'token')
    list_filter = ('created_at', 'expired_at')

@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'ip_address')
    search_fields = ('user__username', 'ip_address')
    list_filter = ('login_time',)
