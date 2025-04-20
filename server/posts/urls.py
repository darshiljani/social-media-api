from django.urls import path

from posts.views.PostCommentViews import PostCommentCreateAPI
from posts.views.PostLikeViews import PostLikeAPI
from posts.views.PostViews import (
    PostCreateAPI,
    PostDeleteAPI,
    PostListAPI,
    PostRetrieveAPI,
    PostUpdateAPI,
)

urlpatterns = [
    path(name="post-list", route="", view=PostListAPI.as_view()),
    path(name="post-retrieve", route="<int:pk>/", view=PostRetrieveAPI.as_view()),
    path(name="post-create", route="create/", view=PostCreateAPI.as_view()),
    path(name="post-update", route="<int:pk>/update/", view=PostUpdateAPI.as_view()),
    path(name="post-delete", route="<int:pk>/delete/", view=PostDeleteAPI.as_view()),
    path(name="post-like", route="<int:post_id>/like/", view=PostLikeAPI.as_view()),
    path(
        name="post-comment-create",
        route="<int:post_id>/comment/",
        view=PostCommentCreateAPI.as_view(),
    ),
]
