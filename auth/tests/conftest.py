import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def new_user_api(client):
    """Регистрация нового пользователя через API."""
    data = {
        'username': 'test',
        'email': 'test@test.ru',
        'password': 'test1234',
    }
    client.post('/api/auth/users/', data=data)
    return data
