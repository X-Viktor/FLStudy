from django.urls import path

from users.api.views import UserListView


urlpatterns = [
    path('', UserListView.as_view())
]
