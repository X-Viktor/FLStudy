import pytest

pytestmark = [pytest.mark.django_db]


def test_get_token(client, new_user_api):
    """Получение JWT."""
    response = client.post('/api/auth/jwt/create/', data=new_user_api)

    assert response.status_code == 200
