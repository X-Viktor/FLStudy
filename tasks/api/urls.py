from django.urls import path

from tasks.api.views import CategoryListView, TaskViewSet

urlpatterns = [
    path('', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='tasks'),
    path('<int:pk>/', TaskViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='task_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
