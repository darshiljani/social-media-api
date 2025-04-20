from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import UserProfile


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email")


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("get_username", "get_user_name", "date_of_birth", "is_active")
    list_filter = ("is_active",)
    search_fields = ("user__username", "user__name", "user__email")

    def get_username(self, obj):
        return obj.user.username

    def get_user_name(self, obj):
        return obj.user.name

    get_username.short_description = "Username"
    get_username.admin_order_field = "user__username"

    get_user_name.short_description = "Name"
    get_user_name.admin_order_field = "user__name"


admin.site.register(model_or_iterable=get_user_model(), admin_class=UserAdmin)
admin.site.register(model_or_iterable=UserProfile, admin_class=UserProfileAdmin)
