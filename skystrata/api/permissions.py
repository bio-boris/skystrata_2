from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `customer`.
        return obj.customer == request.user or request.user.is_staff


class IsOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):
        print("Accessing pages")
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        print("Accessing obj")
        return obj.customer == request.user
