from constants.exceptions import ResourceNotFound
from constants.permissions import IsOwner
from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404
from posts.models import Posts
from posts.serializers.PostSerializers import PostReadSerializer, PostWriteSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class PostListAPI(ListAPIView):
    """API endpoint that allows posts to be viewed.

    This view inherits from ListAPIView and provides a read-only endpoint
    for viewing all posts in the system.

    Returns:
        list: A list of posts with the following information:
            - Post data
            - Number of likes
            - Number of comments

    Examples:
        GET /api/posts/
        GET /api/posts/?ordering=created_at
        GET /api/posts/?ordering=-created_at

    """

    permission_classes = (AllowAny,)
    queryset = Posts.objects.all().annotate(
        like_count=Count("likes", distinct=True),
        comment_count=Count("comments", distinct=True),
    )
    serializer_class = PostReadSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "last_updated_at"]


class PostRetrieveAPI(RetrieveAPIView):
    """Retrieve API view for Posts.

    This view handles retrieval of individual post objects, including their like and comment counts.

    Raises:
        ResourceNotFound: When requested post does not exist
    Example:
        GET /api/posts/<post_id>/
        Returns detailed information about a specific post including:
        - Post data
        - Like count
        - Comment count

    """

    permission_classes = (AllowAny,)
    queryset = Posts.objects.all()
    serializer_class = PostReadSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            "Expected view %s to be called with a URL keyword argument "
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            "attribute on the view correctly."
            % (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, **filter_kwargs)
            self.check_object_permissions(self.request, obj)
            return obj
        except Http404:
            raise ResourceNotFound(detail="Post does not exist")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data["like_count"] = instance.likes.count()
        data["comment_count"] = instance.comments.count()
        return Response(data)


class PostCreateAPI(CreateAPIView):
    """API endpoint for creating new posts.

    This view allows authenticated users to create new posts in the system.

    Returns:
        Response: Returns a 201 Created response with the created post data if successful.
            Returns appropriate error responses if validation fails.

    Raises:
        ValidationError: If the request data is invalid.
        PermissionDenied: If the user is not authenticated.

    """

    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()
    serializer_class = PostWriteSerializer


class PostUpdateAPI(UpdateAPIView):
    """Updates an existing post instance.

    This API endpoint allows authenticated users to update their own posts.

    Args:
        None directly (uses URL parameters)

    Returns:
        Response with updated post data if successful

    Raises:
        PermissionDenied: If user is not the owner of the post
        NotAuthenticated: If user is not authenticated
        ValidationError: If invalid data is provided

    """

    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Posts.objects.all()
    serializer_class = PostWriteSerializer


class PostDeleteAPI(DestroyAPIView):
    """API endpoint for deleting a specific post.

    This view inherits from DestroyAPIView and allows authenticated users to delete
    their own posts. It requires both authentication and ownership verification.

    Permissions:
        - User must be authenticated
        - User must be the owner of the post

    HTTP Methods:
        - DELETE: Delete a specific post

    Returns:
        Response with status 204 No Content on successful deletion

    Raises:
        404: If post with given ID is not found
        403: If user is not the owner of the post
        401: If user is not authenticated

    """

    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Posts.objects.all()
