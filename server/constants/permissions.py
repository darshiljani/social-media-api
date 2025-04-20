from django.conf import settings
from rest_framework.permissions import BasePermission


class InternalIPPermission(BasePermission):
    message = "Forbidden"

    def has_permission(self, request, view):  # type: ignore
        ip_addr = request.META.get("REMOTE_ADDR")
        if ip_addr in settings.INTERNAL_IPS:
            return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
