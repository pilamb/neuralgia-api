from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # GET, HEAD or OPTIONS requests allowed.
        if request.method in permissions.SAFE_METHODS:
            return True

        # NOqa: a 500 is thrown since Anonymous is not instance of User
        return obj.owner == request.user