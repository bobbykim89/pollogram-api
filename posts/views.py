from rest_framework.generics import (
    ListCreateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView)
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import PostModel, PostLikeModel
from .serializers import PostSerializer, PostLikeSerializer
from .permissions import IsAuthorOrAdmin
from user_profiles.models import ProfileModel
from cloudinary import uploader
from uuid import uuid4

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
        file = self.request.data.get('image')
        upload_data = uploader.upload(file=file, folder='pollogram/post')
        image_id: str = upload_data['public_id']
        title = str(uuid4())
        content = serializer.validated_data.get('content') or None
        serializer.save(user=current_user_profile, title=title,
                        image_id=image_id, content=content)
