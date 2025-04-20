from django.urls import path

from users.views.UserProfileViews import (
    UserListAPI,
    UserProfileDeleteAPI,
    UserProfileRetrieveAPI,
    UserProfileUpdateAPI,
)

urlpatterns = [
    path(name="user-list", route="", view=UserListAPI.as_view()),
    path(
        name="user-retrieve",
        route="<int:user_id>/",
        view=UserProfileRetrieveAPI.as_view(),
    ),
    path(
        name="user-profile-update",
        route="<int:user_id>/update/",
        view=UserProfileUpdateAPI.as_view(),
    ),
    path(
        name="user-profile-delete",
        route="<int:user_id>/delete/",
        view=UserProfileDeleteAPI.as_view(),
    ),
]
