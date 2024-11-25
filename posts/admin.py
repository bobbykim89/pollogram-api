from django.contrib import admin
from .models import PostModel, PostLikeModel

# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user', 'content', 'created_at', 'updated_at']


class PostLikeModelAdmin(admin.ModelAdmin):
    list_filter = ['user_profile', 'liked_post']
    list_display = ['user_profile', 'liked_post', 'created_at']


admin.site.register(PostModel, PostModelAdmin)
admin.site.register(PostLikeModel, PostLikeModelAdmin)
