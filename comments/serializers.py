from rest_framework import serializers
from .models import CommentModel, CommentLikeModel
from user_profiles.serializers import ProfileSerializerMinimal
from posts.serializers import PostSerializerMinimal


class CommentSerializer(serializers.ModelSerializer):
    user = ProfileSerializerMinimal(read_only=True)
    # post = PostSerializerMinimal(read_only=True)
    liked_users = serializers.SerializerMethodField()

    class Meta:
        model = CommentModel
        fields = ['id', 'user', 'post', 'text',
                  'liked_users', 'created_at']

    def get_liked_users(self, obj):
        liked_users = CommentLikeModel.objects.filter(liked_comment=obj)
        return CommentLikedUserSerializer(liked_users, many=True).data


class CommentLikeSerializer(serializers.ModelSerializer):
    user_profile = serializers.CharField(read_only=True)
    liked_comment = serializers.CharField(read_only=True)

    class Meta:
        model = CommentLikeModel
        fields = ['user_profile', 'liked_comment', 'created_at']


class CommentLikedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikeModel
        fields = ['id', 'user_profile', 'created_at']
