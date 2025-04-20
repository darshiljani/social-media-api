from django.urls import path

from authentication.views.LoginView import LoginAPI
from authentication.views.RegisterView import UserRegistrationAPI

urlpatterns = [
    path(
        name="user-registration", route="register/", view=UserRegistrationAPI.as_view()
    ),
    path(name="login", route="login/", view=LoginAPI.as_view()),
]
