from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Класс проверки является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(BasePermission):
    """Класс проверки является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
