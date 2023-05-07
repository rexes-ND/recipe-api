"""
Views for the user API.
"""
from rest_framework import (
    generics,
    authentication,
    permissions
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    # Customizer auth using email and password
    serializer_class = AuthTokenSerializer
    # For nice UI
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# For retrieving and updating the obj in DB
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    # Make sure user using the API is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # HTTP GET
    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
