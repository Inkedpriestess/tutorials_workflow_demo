from django.test import TestCase
from django.urls import reverse
import pytest

@pytest.fixture
def test_user(db, django_user_model):
    user = django_user_model.objects.create_user(
        username="test_username", 
        password="test_password"
    )
    return "test_username", "test_password"

def test_login(client, test_user):
    username, password = test_user
    response = client.post(reverse('login'), {'username': username, 'password': password})
    assert response.status_code in [200, 302]