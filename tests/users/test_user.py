import pytest

from rest_framework import status


@pytest.mark.django_db
def test_user_register(client, user_data):
    response = client.post('/auth/register/', user_data)
    data = response.data
    assert response.status_code == status.HTTP_201_CREATED
    assert user_data.get('username') == data.get('username')
    assert 'password' not in data
    

@pytest.mark.django_db
def test_user_login(client, credentials):
    response = client.post('/auth/login/', credentials)
    token = response.data.get('token')
    assert response.status_code == status.HTTP_200_OK
    assert token.isalnum() and len(token) == 64


@pytest.mark.django_db
def test_user_refresh(auth_client, credentials):
    response = auth_client.post('/auth/refresh/', credentials)
    token = response.data.get('token')
    assert response.status_code == status.HTTP_200_OK
    assert token.isalnum() and len(token) == 64


@pytest.mark.django_db
def test_user_me(auth_client):
    response = auth_client.get('/auth/me/')
    assert response.status_code == status.HTTP_200_OK
    

@pytest.mark.django_db
def test_user_logout(auth_client):
    response = auth_client.post('/auth/logout/')
    assert response.status_code == status.HTTP_204_NO_CONTENT