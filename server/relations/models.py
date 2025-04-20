from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class UserRelationship(models.Model):
    from_user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="following_relation"
    )
    to_user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="follower_relation"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("from_user", "to_user")
        verbose_name = "user relation"
        verbose_name_plural = "user relations"

    def __str__(self):
        return f"{self.from_user.username} -> {self.to_user.username}"
