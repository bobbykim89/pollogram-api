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
    liked_users = models.ManyToManyField(
        ProfileModel, related_name='liked_posts', blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
