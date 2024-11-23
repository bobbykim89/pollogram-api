from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import (
    UserSerializer,
    UserSignupSerializer,
    UserPasswordChangeSerializer,
    CustomTokenObtainPairSerializer
)
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


class UserDetailApiView(RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class SignupAPIView(CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT tokens for the user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Return response with tokens
        response_data = {
            "user": {
                "username": user.username,
                "email": user.email,
            },
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        return Response(response_data, status=201)


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req):
        serializer = UserPasswordChangeSerializer(
            data=req.data, context={'request': req})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Password updated successfully!'})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = []
