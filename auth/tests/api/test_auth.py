import pytest

pytestmark = [pytest.mark.django_db]


def test_user_registration(api_client):
    """Регистрация пользователя через API."""
    data = {
        'username': 'test1',
        'email': 'test1@test.ru',
        'password': 'test1234',
    }
    response = api_client.post('/api/auth/users/', data=data)
    assert response.status_code == 201


def test_get_token(api_client, user):
    """Получение JWT."""
    url = '/api/auth/jwt/create/'
    login_data = {
        'username': user.username,
        'password': 'test1234',
    }
    response = api_client.post(url, data=login_data)

    assert response.data['access'] is not None
    assert response.status_code == 200
