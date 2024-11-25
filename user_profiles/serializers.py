from rest_framework import serializers, validators
from .models import ProfileModel, ProfileFollowingModel
from users.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProfileModel
        fields = ['id', 'user', 'username', 'profile_picture',
                  'profile_text', 'created_at', 'updated_at']


class ProfileFollowingSerializer(serializers.ModelSerializer):
    user_profile = serializers.CharField(required=False)
    following_user_id = serializers.CharField(required=False)

    class Meta:
        model = ProfileFollowingModel
        fields = ['user_profile', 'following_user_id', 'created_at']
        validators = [
            validators.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['user_profile', 'following_user_id']
            )
        ]
