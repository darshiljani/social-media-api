from posts.models import Posts
from rest_framework import serializers


class PostReadSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="user.name", read_only=True)
    author_username = serializers.CharField(source="user.username", read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Posts
        fields = "__all__"


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["content"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data=validated_data)
