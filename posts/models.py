from django.db import models
from django.utils.timezone import now
from user_profile.models import UserProfile

# Create your models here.


class PostModel(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    liked_users = models.ManyToManyField(
        UserProfile, related_name='liked_posts', blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
