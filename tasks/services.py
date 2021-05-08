from rest_framework import permissions


from tasks.api.serializers import (TaskCreateSerializer,
                                   TaskSerializer)
from tasks.permissions import IsOwner


def set_serializer_for_action(action):
    if action in ['create', 'update']:
        return TaskCreateSerializer
    return TaskSerializer


def set_permission_for_action(action):
    if action in ['destroy', 'update']:
        # Разрешаем редактировать или удалять задачу только владельцу
        return [IsOwner]
    elif action == 'create':
        # Разрешаем создавать задачу только авторизованным пользователям
        return [permissions.IsAuthenticated]
    else:
        return [permissions.AllowAny]
