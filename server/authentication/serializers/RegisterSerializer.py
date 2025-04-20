from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())],
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "name", "password")

        extra_kwargs = {"name": {"required": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            name=validated_data["name"],
        )
        user.set_password(raw_password=validated_data["password"])
        user.save()
        return user
