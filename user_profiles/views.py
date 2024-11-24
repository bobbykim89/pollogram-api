from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProfileSerializer
from .models import ProfileModel

# Create your views here.


class CurrentUserProfileAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        current_user = self.request.user
        current_user_profile = self.queryset.get(user=current_user)
        if current_user_profile is not None:
            return current_user_profile


class UserProfileCreateListAPIView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserProfileDetailAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProfileModel.objects.all()
    lookup_field = 'pk'
