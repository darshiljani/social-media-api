from django.contrib import admin
from utils.common import shorten_text

from posts.models import PostComments, PostLikes, Posts


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        "get_author",
        "content",
        "created_at",
        "last_updated_at",
    )
    search_fields = ("user__username", "user__name")
    list_filter = ("user__username", "created_at")

    def get_author(self, obj):
        return f"{obj.user.username} : {obj.user.name}"

    get_author.short_description = "Author"
    get_author.admin_order_field = "user__username"


class PostLikeAdmin(admin.ModelAdmin):
    list_display = ("get_liked_by", "get_post_content")

    search_fields = ("liked_by__username", "liked_by__name", "post__content")

    def get_liked_by(self, obj):
        return f"{obj.liked_by.username} : {obj.liked_by.name}"

    def get_post_content(self, obj):
        return shorten_text(content=obj.post.content)

    get_liked_by.short_description = "Liked by"
    get_liked_by.admin_order_field = "user__username"

    get_post_content.short_description = "Post"
    get_post_content.admin_order_field = "post__content"


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "post", "get_post_content", "get_author")
    search_fields = ("user__username", "user__name", "post__content", "content")

    def get_author(self, obj):
        return f"{obj.user.username} : {obj.user.name}"

    def get_post_content(self, obj):
        return shorten_text(content=obj.post.content)

    get_author.short_description = "Author"
    get_author.admin_order_field = "user__username"

    get_post_content.short_description = "Post"
    get_post_content.admin_order_field = "post__content"


admin.site.register(model_or_iterable=Posts, admin_class=PostsAdmin)
admin.site.register(model_or_iterable=PostLikes, admin_class=PostLikeAdmin)
admin.site.register(model_or_iterable=PostComments, admin_class=PostCommentAdmin)
