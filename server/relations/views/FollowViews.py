from constants.exceptions import InvalidRequest, ResourceNotFound
from django.contrib.auth import get_user_model
from relations.models import UserRelationship
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class FollowToggleAPI(APIView):
    """Toggle follow/unfollow relationship between users.

    This API endpoint allows authenticated users to follow or unfollow other users.
    If a follow relationship already exists, it will be removed (unfollow).
    If no relationship exists, it will be created (follow).

    Args:
        request: The HTTP request object containing user authentication details
        to_user_id (int): The ID of the user to follow/unfollow
    Returns:
        Response: JSON response containing:
            - following (bool): True if a new follow relationship was created,
                              False if an existing relationship was removed
    Raises:
        InvalidRequest: If a user attempts to follow themselves
        ResourceNotFound: If the target user does not exist
    Permission:
        Requires user authentication

    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, to_user_id):
        User = get_user_model()
        from_user = request.user
        if from_user.id == to_user_id:
            raise InvalidRequest(detail="You cannot follow yourself")
        try:
            to_user = User.objects.get(id=to_user_id)
            relation, created = UserRelationship.objects.get_or_create(
                from_user=from_user,
                to_user=to_user,
            )
            if not created:
                relation.delete()
            return Response(data={"following": created})
        except User.DoesNotExist:
            raise ResourceNotFound(detail="User not found")
