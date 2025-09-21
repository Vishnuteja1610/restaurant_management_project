from rest_framework import generics, permissions
from .serializers import UserProfileSerializer

class UserProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticaticated]

    def get_object(self):
        return self.request.user
        