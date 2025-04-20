from authentication.serializers.RegisterSerializer import UserRegistrationSerializer
from constants.exceptions import InvalidRequest
from constants.status import STATUS
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class UserRegistrationAPI(APIView):
    """User Registration API View.

    This view handles the registration of new users in the system.

    Methods:
        post(request): Handles POST requests for user registration.

    Example:
        To register a new user, make a POST request with user data:
        POST /api/register/
        {
            "username": "newuser",
            "email": "user@example.com",
            "password": "secure_password"
        }

    """

    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "User registered successfully!"}, status=STATUS.CREATED
            )
        else:
            raise InvalidRequest(detail=serializer.errors)
