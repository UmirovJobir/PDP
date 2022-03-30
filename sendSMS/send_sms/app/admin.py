from django.contrib import admin

from .models import Send, User


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ("__all__",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user_number', 'message_id', 'text')
