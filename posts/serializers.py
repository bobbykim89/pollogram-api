from rest_framework import serializers
from .models import PostLikeModel, PostModel
from user_profiles.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = PostModel
        fields = ['id', 'user', 'title', 'content',
                  'image_id', 'created_at', 'updated_at']
