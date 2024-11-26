from rest_framework import permissions
from user_profiles.models import ProfileModel


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        current_user = request.user
        current_user_profile = ProfileModel.objects.get(user=current_user)
        print(current_user_profile)
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        return obj.user == current_user_profile
