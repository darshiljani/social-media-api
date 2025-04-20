from django.urls import path

from relations.views.FollowViews import FollowToggleAPI

urlpatterns = [
    path(
        name="follow-toggle",
        route="toggle-follow/<int:to_user_id>/",
        view=FollowToggleAPI.as_view(),
    )
]
