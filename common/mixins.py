from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthorOrAuthReadOnly


class JWTAuthAndPermissionsMixin():
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAuthReadOnly]
