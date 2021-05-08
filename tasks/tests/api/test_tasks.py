import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_task_create(api_client, category, token):
    """Добавление задачи."""
    url = reverse('tasks')

    task_data = {
        'category': category.id,
        'title': 'Test create task',
        'description': 'Test description',
        'reward': '1000',
    }

    # Неавторизованный пользователь
    response = api_client.post(url, data=task_data)
    assert response.status_code == 401

    # Авторизованный пользователь
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['access'])
    response = api_client.post(url, data=task_data)
    assert response.data['title'] == 'Test create task'
    assert response.status_code == 201


def test_task_edit(api_client, task, token):
    """Редактирование задачи."""
    url = reverse('task_detail', kwargs={'pk': task.pk})
    task_data = {
        'category': task.category.pk,
        'title': 'Test edit title',
        'description': task.description,
        'reward': task.reward,
    }
    # Неавторизованный пользователь
    response = api_client.put(url, data=task_data)
    assert response.status_code == 401

    # Авторизованный пользователь
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['access'])
    response = api_client.put(url, data=task_data)
    assert response.data['title'] == 'Test edit title'
    assert response.status_code == 200


def test_task_delete(api_client, task, token):
    """Удаление задачи."""
    url = reverse('task_detail', kwargs={'pk': task.pk})

    # Неавторизованный пользователь
    response = api_client.delete(url)
    assert response.status_code == 401

    # Авторизованный пользователь
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['access'])
    response = api_client.delete(url)
    assert response.status_code == 204


def test_task_detail(api_client, task):
    """Получение подробностей задачи."""
    url = reverse('task_detail', kwargs={'pk': task.pk})
    response = api_client.get(url)

    assert response.data['title'] == task.title
    assert response.status_code == 200


def test_task_list(api_client):
    """Получение всех задач."""
    url = reverse('tasks')
    response = api_client.get(url)

    assert response.status_code == 200
