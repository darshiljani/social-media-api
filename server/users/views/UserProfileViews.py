from constants.exceptions import ResourceNotFound
from constants.permissions import IsOwner
from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.filters import UserFilter
from users.models import UserProfile
from users.serializers.UserProfileSerializers import (
    UserProfileReadSerializer,
    UserProfileUpdateSerializer,
)


class UserListAPI(ListAPIView):
    """Provides API endpoint to retrieve list of user profiles.

    This view allows listing all user profiles with their follower counts.
    No authentication is required to access this endpoint.

    Returns:
        List[dict]: List of user profile data including:
            - Basic profile information
            - Follower count for each user

    Example Response:
        [
            {
                "id": 1,
                "username": "user1",
                "follower_count": 5,
                ...
            },
            ...
        ]

    """

    permission_classes = (AllowAny,)

    queryset = UserProfile.objects.all().annotate(
        follower_count=Count("user__follower_relation")
    )
    serializer_class = UserProfileReadSerializer
    filterset_class = UserFilter


class UserProfileRetrieveAPI(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileReadSerializer
    lookup_field = "user_id"

    def get_object(self):
        try:
            profile = UserProfile.objects.get(user_id=self.kwargs["user_id"])
            if not profile.is_active:
                raise ResourceNotFound(
                    detail="Profile does not exist or might be inactive"
                )
            return profile
        except UserProfile.DoesNotExist:
            print("Does not exist")
            raise ResourceNotFound(detail="Profile does not exist or might be inactive")


class UserProfileUpdateAPI(UpdateAPIView):
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
    queryset = UserProfile.objects.all()
    lookup_field = "user_id"
    serializer_class = UserProfileUpdateSerializer


class UserProfileDeleteAPI(DestroyAPIView):
    queryset = UserProfile.objects.all()
    lookup_field = "user_id"
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
