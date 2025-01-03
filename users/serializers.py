from typing import Any, Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, hashers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user_profiles.models import ProfileModel

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Passwords must match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = hashers.make_password(
            validated_data['password'])
        user = User.objects.create(**validated_data)
        ProfileModel.objects.create(user=user, username=user.username)
        return user


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(
        write_only=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old Password is incorrect')
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        username_or_email = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(request=self.context.get(
            'request'), username=username_or_email, password=password)
        if user is None:
            user = authenticate(
                request=self.context.get('request'),
                username=User.objects.filter(email=username_or_email).values_list(
                    'username', flat=True).first(),
                password=password
            )
            if user:
                attrs['username'] = user.username
        if not user:
            raise serializers.ValidationError('Invalid Credentials')

        return super().validate(attrs)
