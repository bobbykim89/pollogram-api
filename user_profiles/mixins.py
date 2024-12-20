from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from .permissions import IsAuthorOrAuthReadOnly


class UserProfileJWTAuthAndPermissionsMixin():
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAuthReadOnly]


class UserProfileJWTAuthOnlyPermissionsMixin():
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
