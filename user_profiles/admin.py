from django.contrib import admin
from .models import ProfileModel

# Register your models here.


class ProfileModelAdmin(admin.ModelAdmin):
    list_filter = ['username', 'user']
    list_display = ['username', 'user', 'created_at', 'updated_at']


admin.site.register(ProfileModel, ProfileModelAdmin)
