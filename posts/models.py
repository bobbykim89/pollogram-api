from django.db import models
from django.utils.timezone import now
from user_profiles.models import ProfileModel

# Create your models here.


class PostModel(models.Model):
    user = models.ForeignKey(
        ProfileModel, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    image_id = models.CharField(
        max_length=255, blank=True, null=True)  # Can store image URLs or paths
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class PostLikeModel(models.Model):
    user_profile = models.ForeignKey(
        ProfileModel, related_name='likes', on_delete=models.CASCADE)
    liked_post = models.ForeignKey(
        PostModel, related_name='liked_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_profile', 'liked_post'],
                name='unique_likes'
            )
        ]
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.user_profile} likes {self.liked_post}'
