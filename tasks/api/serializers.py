from rest_framework import serializers

from tasks.models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['category', 'title', 'description', 'reward']

    def create(self, validated_data):
        """Создаем задачу от лица авторизованного пользователя."""
        return Task.objects.create(customer=self.context['request'].user,
                                   **validated_data)


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Task
        fields = ['status', 'category', 'title', 'description',
                  'reward', 'customer', 'date_creation']
