from rest_framework import serializers
from .models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id', 'user', 'username', 'profile_picture',
                  'profile_text', 'created_at', 'updated_at']
