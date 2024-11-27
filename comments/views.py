from rest_framework.generics import (
    ListCreateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from .permissions import IsAuthorOrAdmin
from .serializers import CommentSerializer, CommentLikeSerializer
from .models import CommentModel, CommentLikeModel
from user_profiles.models import ProfileModel
from posts.models import PostModel

# Create your views here.


class CommentListCreatePerPostAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        target_post = PostModel.objects.get(id=post_id)
        comments_on_post = CommentModel.objects.filter(post=target_post)
        return comments_on_post

    def perform_create(self, serializer):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        post_id = self.kwargs['post_id']
        post = PostModel.objects.get(id=post_id)
        text = serializer.validated_data.get('text')
        serializer.save(user=current_user_profile, post=post, text=text)


class CommentDeleteAPIView(DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    lookup_field = 'pk'


class CommentLikeCreateAPIView(CreateAPIView):
    serializer_class = CommentLikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    queryset = CommentLikeModel.objects.all()

    def perform_create(self, serializer):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        target_comment = CommentModel.objects.get(id=self.kwargs['pk'])
        if target_comment:
            serializer.save(user_profile=current_user_profile,
                            liked_comment=target_comment)


class CommentUnlikeDestroyAPIView(DestroyAPIView):
    serializer_class = CommentLikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    queryset = CommentLikeModel.objects.all()

    def get_object(self):
        current_user = self.request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        target_comment = CommentModel.objects.get(id=self.kwargs['pk'])
        if not target_comment:
            raise NotFound('Comment not found.')
        try:
            return self.queryset.get(user_profile=current_user_profile, liked_comment=target_comment)
        except CommentModel.DoesNotExist:
            raise NotFound('You haven\'t liked this post.')
