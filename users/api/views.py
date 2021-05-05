from rest_framework import generics

from users.api import serializers
from users.models import User


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
