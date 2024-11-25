from rest_framework import serializers
from .models import ProfileModel, ProfileFollowingModel
from users.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    user = UserSerializer(read_only=True)
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = ProfileModel
        fields = ['id', 'user', 'username', 'profile_picture',
                  'profile_text', 'following', 'followers', 'created_at', 'updated_at']

    def get_following(self, instance):
        return FollowingSerializer(instance.following.all(), many=True).data

    def get_followers(self, instance):
        return FollowerSerializer(instance.followers.all(), many=True).data


class ProfileFollowingSerializer(serializers.ModelSerializer):
    user_profile = serializers.CharField(read_only=True)
    following_user_id = serializers.CharField(read_only=True)

    class Meta:
        model = ProfileFollowingModel
        fields = ['user_profile', 'following_user_id', 'created_at']


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFollowingModel
        fields = ['id', 'following_user_id', 'created_at']


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFollowingModel
        fields = ['id', 'user_profile', 'created_at']
