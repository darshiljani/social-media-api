from authentication.serializers.LoginSerializer import LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginAPI(TokenObtainPairView):
    """Login API endpoint for user authentication.

    This API endpoint extends TokenObtainPairView to handle user login requests
    and generate JWT token pairs (access and refresh tokens).

    Returns:
        Response: JSON response containing:
            - access_token: JWT access token
            - refresh_token: JWT refresh token
    Raises:
        ValidationError: If provided credentials are invalid
        AuthenticationFailed: If user account is inactive or credentials are incorrect

    """

    serializer_class = LoginSerializer
