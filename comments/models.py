from django.db import models
from django.utils.timezone import now
from user_profiles.models import ProfileModel
from posts.models import PostModel

# Create your models here.


class CommentModel(models.Model):
    user = models.ForeignKey(
        ProfileModel, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        PostModel, on_delete=models.CASCADE, related_name='comments_post')
    text = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text


class CommentLikeModel(models.Model):
    user_profile = models.ForeignKey(
        ProfileModel, related_name='comment_liked_users', on_delete=models.CASCADE)
    liked_comment = models.ForeignKey(
        CommentModel, related_name='liked_comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_profile', 'liked_comment'],
                name='unique_comment_likes'
            )
        ]
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.user_profile} likes {self.liked_comment}'
