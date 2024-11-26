from rest_framework.generics import (
    ListCreateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound, APIException
from django.core.files.uploadedfile import TemporaryUploadedFile
from .models import PostModel, PostLikeModel
from .serializers import PostSerializer, PostLikeSerializer
from .permissions import IsAuthorOrAdmin
from .composables import validate_extension
from user_profiles.models import ProfileModel
from cloudinary import uploader

# Create your views here.


class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    parser_classes = [MultiPartParser, JSONParser]

    def perform_create(self, serializer):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        content = serializer.validated_data.get('content') or None
        file: TemporaryUploadedFile = self.request.data.get('image')
        if validate_extension(file.name):
            upload_data = uploader.upload(file=file, folder='pollogram/post')
            image_id: str = upload_data['public_id']
            serializer.save(user=current_user_profile,
                            image_id=image_id, content=content)
        else:
            raise APIException('Unsupported file type.')


class PostDetailDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        uploader.destroy(instance.image_id)
        return super().perform_destroy(instance)


class PostLikeCreateAPIView(CreateAPIView):
    serializer_class = PostLikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    queryset = PostLikeModel.objects.all()

    def perform_create(self, serializer):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        target_post = PostModel.objects.get(id=self.kwargs['pk'])
        if target_post:
            serializer.save(user_profile=current_user_profile,
                            liked_post=target_post)
        return super().perform_create(serializer)


class PostUnlikeDestroyAPIView(DestroyAPIView):
    serializer_class = PostLikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    queryset = PostLikeModel.objects.all()

    def get_object(self):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        target_post = PostModel.objects.get(id=self.kwargs['pk'])
        if not target_post:
            raise NotFound('Post not found.')
        try:
            return self.queryset.get(user_profile=current_user_profile, liked_post=target_post)
        except PostLikeModel.DoesNotExist:
            raise NotFound("You haven't liked this post.")
