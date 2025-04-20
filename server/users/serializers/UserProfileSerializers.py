from rest_framework import serializers
from users.models import UserProfile


class UserProfileReadSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    name = serializers.CharField(source="user.name", read_only=True)
    follower_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", required=False)
    name = serializers.CharField(source="user.name", required=False)
    email = serializers.EmailField(source="user.email", required=False)

    class Meta:
        model = UserProfile
        fields = "__all__"

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        user = instance.user

        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
