from rest_framework import permissions


class IsAuthorOrAuthReadOnly(permissions.BasePermission):
    """
    Custom permission for model:
    - Admin or staff can perform all actions.
    - The author of the post can perform all actions.
    - Authenticated users can read posts.
    - Unauthenticated users cannot do anything.
    """

    def has_permission(self, request, view):
        # Allow authenticated users to perform safe (read-only) actions
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True

         # For unsafe actions, further checks will be done in `has_object_permission`
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admins or staff can perform all actions
        if request.user.is_staff:
            return True

        # The author of the post can perform all actions
        if obj.user == request.user:
            return True

        # Authenticated users can only read the object
        if request.method in permissions.SAFE_METHODS:
            return True

        # Unauthenticated users cannot do anything
        return False
