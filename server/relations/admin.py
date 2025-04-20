from django.contrib import admin

from relations.models import UserRelationship


# Register your models here.
class UserRelationshipAdmin(admin.ModelAdmin):
    list_display = (
        "get_from_user",
        "get_to_user",
    )
    search_fields = (
        "from_user__username",
        "to_user__username",
        "from_user__name",
        "to_user__name",
    )

    def get_from_user(self, obj):
        return obj.from_user.username

    def get_to_user(self, obj):
        return obj.to_user.username

    get_from_user.short_description = "From user"
    get_from_user.admin_order_field = "from_user__username"

    get_to_user.short_description = "To user"
    get_to_user.admin_order_field = "to_user__username"


admin.site.register(
    model_or_iterable=UserRelationship, admin_class=UserRelationshipAdmin
)
