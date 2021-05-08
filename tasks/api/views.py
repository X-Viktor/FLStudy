from rest_framework import generics, viewsets

from tasks.api.serializers import CategorySerializer
from tasks.models import Category, Task
from tasks.services import (set_permission_for_action,
                            set_serializer_for_action)


class CategoryListView(generics.ListAPIView):
    """Отображение категорий."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Операции с задачами."""
    queryset = Task.objects.all().select_related('category', 'customer')

    def get_permissions(self):
        """Устанавливаем уровни доступа для действий с заказами."""
        self.permission_classes = set_permission_for_action(self.action)
        return super(TaskViewSet, self).get_permissions()

    def get_serializer_class(self):
        """Устанавливаем serializer в зависимости от действия."""
        return set_serializer_for_action(self.action)
