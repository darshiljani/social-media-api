from constants.exceptions import ResourceNotFound
from posts.models import PostComments, Posts
from posts.serializers.PostCommentSerializers import PostCommentWriteSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated


class PostCommentCreateAPI(CreateAPIView):
    """API endpoint for creating post comments.

    This view allows authenticated users to create comments on existing posts.

    Raises:
        ResourceNotFound: When the referenced post does not exist
    Example:
        POST /api/posts/{post_id}/comments/
        {
            "content": "This is a comment"
        }

    """

    permission_classes = (IsAuthenticated,)
    queryset = PostComments.objects.all()
    serializer_class = PostCommentWriteSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        try:
            post = Posts.objects.get(id=post_id)
            serializer.save(
                post=post,
            )
        except Posts.DoesNotExist:
            raise ResourceNotFound(detail="Post does not exist")
