import cloudinary.uploader
from rest_framework.generics import (
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView, ListAPIView,
    CreateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound, APIException
from django.core.files.uploadedfile import TemporaryUploadedFile
from .serializers import ProfileSerializer, ProfileFollowingSerializer
from .models import ProfileModel, ProfileFollowingModel
from posts.composables import validate_extension
from .mixins import UserProfileJWTAuthAndPermissionsMixin, UserProfileJWTAuthOnlyPermissionsMixin
import cloudinary

# Create your views here.


class CurrentUserProfileAPIView(UserProfileJWTAuthAndPermissionsMixin, RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()

    def get_object(self):
        current_user = self.request.user
        current_user_profile = self.queryset.get(user=current_user)
        if current_user_profile is not None:
            return current_user_profile


class CurrentUserUpdateProfilePictureAPIView(UserProfileJWTAuthAndPermissionsMixin, UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    parser_classes = [MultiPartParser, JSONParser]

    def get_object(self):
        current_user = self.request.user
        current_user_profile = self.queryset.get(user=current_user)
        if current_user_profile is not None:
            return current_user_profile

    def perform_update(self, serializer):
        file: TemporaryUploadedFile = self.request.data.get('image')
        if validate_extension(file.name):
            obj = serializer.instance
            if obj.profile_picture is not None:
                cloudinary.uploader.destroy(obj.profile_picture)
            upload_data = cloudinary.uploader.upload(
                file=file, folder='pollogram/profile')
            image_id: str = upload_data['public_id']
            obj.profile_picture = image_id
            serializer.save()
        else:
            raise APIException('Unsupported file type.')


class UserProfileListAPIView(UserProfileJWTAuthOnlyPermissionsMixin, ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()


class UserProfileDetailAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProfileModel.objects.all()
    lookup_field = 'pk'


class UserProfileCreateFollowAPIView(UserProfileJWTAuthOnlyPermissionsMixin, CreateAPIView):
    serializer_class = ProfileFollowingSerializer
    queryset = ProfileFollowingModel.objects.all()

    def perform_create(self, serializer):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        target_user_profile = ProfileModel.objects.get(id=self.kwargs['pk'])
        if target_user_profile:
            serializer.save(user_profile=current_user_profile,
                            following_user_id=target_user_profile)


class UserProfileDestroyFollowAPIView(UserProfileJWTAuthOnlyPermissionsMixin, DestroyAPIView):
    serializer_class = ProfileFollowingSerializer
    queryset = ProfileFollowingModel.objects.all()

    def get_object(self):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        target_user_profile = ProfileModel.objects.get(
            id=self.kwargs['pk'])

        if not target_user_profile:
            raise NotFound("Target user profile doesn't exist.")
        try:
            return self.queryset.get(user_profile=current_user_profile,
                                     following_user_id=target_user_profile)
        except ProfileFollowingModel.DoesNotExist:
            raise NotFound("You are not following this user")
