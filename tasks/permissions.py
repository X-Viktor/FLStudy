from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Разрешение, позволяющее только владельцам объекта редактировать его."""
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
