from django.contrib import admin
from .models import ProfileModel, ProfileFollowingModel

# Register your models here.


class ProfileModelAdmin(admin.ModelAdmin):
    list_filter = ['username', 'user']
    list_display = ['username', 'user', 'created_at', 'updated_at']


class ProfileFollowingModelAdmin(admin.ModelAdmin):
    list_filter = ['user_profile', 'following_user_id']
    list_display = ['user_profile', 'following_user_id', 'created_at']


admin.site.register(ProfileModel, ProfileModelAdmin)
admin.site.register(ProfileFollowingModel, ProfileFollowingModelAdmin)
