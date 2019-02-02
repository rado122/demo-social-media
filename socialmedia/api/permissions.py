from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow creator of an object to edit it.
    Assumes the model instance has an `creator` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `creator`.
        return obj.creator == request.user