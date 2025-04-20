from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-last_updated_at", "-created_at"]

    def __str__(self):
        return f"{self.user.username} post from {self.created_at}"


class PostLikes(models.Model):
    post = models.ForeignKey(to=Posts, on_delete=models.CASCADE, related_name="likes")
    liked_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "like"
        verbose_name_plural = "likes"
        unique_together = ["post", "liked_by"]

    def __str__(self):
        return f"{self.post.pk} liked by {self.liked_by.username}"


class PostComments(models.Model):
    post = models.ForeignKey(
        to=Posts, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.CharField(max_length=255)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment on post {self.post.pk} by {self.user.username}"
