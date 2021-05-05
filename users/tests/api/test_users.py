import pytest
from django.urls import reverse
from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


def test_get_user_list(client):
    """Получение списка пользователей."""
    url = reverse('users')
    response = client.get(url)

    assert response.status_code == 200


def test_new_user_in_list(client):
    """Появление нового пользователя."""
    url = reverse('users')
    response = client.get(url)

    mixer.blend('users.User')
    new_response = client.get(url)

    assert response.content != new_response.content
