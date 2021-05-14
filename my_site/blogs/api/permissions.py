from rest_framework.permissions import BasePermission


class IsPostAuthor(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if obj.author == request.user:
            return True
        return False