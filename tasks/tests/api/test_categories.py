import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_category_list(api_client):
    """Получение всех категорий."""
    url = reverse('categories')
    response = api_client.get(url)

    assert response.status_code == 200
