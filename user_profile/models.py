from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=100)
    profile_picture = models.CharField(
        max_length=255, blank=True, null=True)  # Can store image URLs or paths
    profile_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
