import pytest

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_data():
    """
    User not yet registered
    """
    return dict(
        username='user_bycoders',
        first_name='User',
        last_name='Bycoders',
        email='user@bycoders.com.br',
        password='12345'
    )


@pytest.fixture
def credentials(user_data):
    """
    User already registered
    """
    User = get_user_model()
    user = User(**user_data)
    user.set_password(user_data.get('password'))
    user.save()
    return { 'username': user.username,
             'password': user_data.get('password') }


@pytest.fixture
def auth_client(client, credentials):
    """
    User already registered and logged in
    """
    response = client.post('/auth/login/', credentials)
    token = response.data.get('token')
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    return client
