from rest_framework import serializers
from .models import PostLikeModel, PostModel
from user_profiles.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    user = ProfileSerializer(read_only=True)
    liked_users = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ['id', 'user', 'title', 'content',
                  'image_id', 'liked_users', 'created_at', 'updated_at']

    def get_liked_users(self, obj):
        liked_users = PostLikeModel.objects.filter(liked_post=obj)
        return PostLikedUserSerializer(liked_users, many=True).data


class PostLikeSerializer(serializers.ModelSerializer):
    user_profile = serializers.CharField(read_only=True)
    liked_post = serializers.CharField(read_only=True)

    class Meta:
        model = PostLikeModel
        fields = ['user_profile', 'liked_post', 'created_at']


class PostLikedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikeModel
        fields = ['id', 'user_profile', 'created_at']
