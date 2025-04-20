from constants.exceptions import InvalidRequest
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required!")

        email = self.normalize_email(email=email)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            try:
                validate_password(password=password, user=user)
                user.set_password(password)
            except ValidationError as e:
                raise InvalidRequest(detail=str(e))
        is_created = user.save(using=self._db)
        return is_created

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["name", "email"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class UserProfile(models.Model):
    user = models.OneToOneField(to=Users, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=255, default="")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"

    def __str__(self):
        return f"{self.user.username} profile"
