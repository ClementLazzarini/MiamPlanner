from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_google_user', )
    search_fields = ('email', )
