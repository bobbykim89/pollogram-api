from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

# Create your models here.

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(
        UserModel, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=100)
    profile_picture = models.CharField(
        max_length=255, blank=True, null=True)  # Can store image URLs or paths
    profile_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username


class ProfileFollowingModel(models.Model):
    user_profile = models.ForeignKey(
        ProfileModel, related_name='following', on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(
        ProfileModel, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_profile', 'following_user_id'], name='unique_followers')
        ]
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.user_profile} follows {self.following_user_id}'
