from posts.models import PostComments
from rest_framework import serializers


class PostCommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ["content"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data=validated_data)

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment cannot be empty")
        return value
