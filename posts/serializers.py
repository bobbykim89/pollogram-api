from rest_framework import serializers
from .models import PostLikeModel, PostModel
from user_profiles.serializers import ProfileSerializerMinimal


class PostSerializer(serializers.ModelSerializer):
    user = ProfileSerializerMinimal(read_only=True)
    liked_users = serializers.SerializerMethodField()
    image_id = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = PostModel
        fields = ['id', 'user', 'content',
                  'image_id', 'liked_users', 'created_at', 'updated_at']

    def get_liked_users(self, obj):
        liked_users = PostLikeModel.objects.filter(liked_post=obj)
        return PostLikedUserSerializer(liked_users, many=True).data


class PostSerializerMinimal(serializers.ModelSerializer):
    user = ProfileSerializerMinimal(read_only=True)

    class Meta:
        model = PostModel
        fields = ['id', 'user', 'image_id', 'created_at']


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
