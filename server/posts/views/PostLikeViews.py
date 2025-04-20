from constants.exceptions import ResourceNotFound
from posts.models import PostLikes, Posts
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PostLikeAPI(APIView):
    """API endpoint for handling post like functionality.

    This view allows authenticated users to like/unlike a post. The endpoint toggles the like status:
    if the post wasn't liked by the user, it creates a like; if it was already liked, it removes the like.

    Methods:
        post: Handles the POST request to like/unlike a post
    Raises:
        ResourceNotFound: If the requested post does not exist

    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, post_id):
        try:
            post = Posts.objects.get(id=post_id)
            like, created = PostLikes.objects.get_or_create(
                liked_by=request.user, post=post
            )
            if not created:
                like.delete()
            return Response(data={"liked": created})
        except Posts.DoesNotExist:
            raise ResourceNotFound(detail="Post not found")
