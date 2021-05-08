import pytest
from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


@mixer.middleware('users.User')
def encrypt_password(user):
    """
    Кэширует пароль 'test1234' для всех пользователей,
    созданных во время тестирования.
    """
    user.set_password('test1234')
    return user


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def category(api_client):
    """Пользователь."""
    return mixer.blend('tasks.Category')


@pytest.fixture
def task(api_client, user):
    """Задача."""
    return mixer.blend('tasks.Task', customer=user)


@pytest.fixture
def token(api_client, user):
    """Веб-токен JSON."""
    url = '/api/auth/jwt/create/'
    login_data = {
        'username': user.username,
        'password': 'test1234',
    }
    token = api_client.post(url, login_data)
    return token


@pytest.fixture
def user(api_client):
    """Пользователь."""
    return mixer.blend('users.User')
