from django.contrib import admin
from .models import CommentModel, CommentLikeModel

# Register your models here.


class CommentModelAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user', 'text', 'created_at', 'updated_at']


class CommentLikeModelAdmin(admin.ModelAdmin):
    list_filter = ['user_profile']
    list_display = ['user_profile', 'liked_comment', 'created_at']


admin.site.register(CommentModel, CommentModelAdmin)
admin.site.register(CommentLikeModel, CommentLikeModelAdmin)
