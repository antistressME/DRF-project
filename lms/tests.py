from rest_framework.test import force_authenticate, APITestCase, APIClient
import pytest

from users.models import User


@pytest.fixture
def api_client(db):
    user = User.objects.create(email="test", password="test")
    client = APIClient()
    client.force_authenticate(user=user)
    return client


class TestAuthenticateCreate(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test", password="test")
        self.client.force_authenticate(self.user)

    def test_create_course(self):
        data = {"name": "test", "description": "test"}
        response = self.client.post("/materials/", data)
        assert response.status_code == 201
        assert response.json() == data

    def test_create_lesson(self):
        data = {"name": "test", "description": "test", "course": 1}
        response = self.client.post("/materials/lesson/create/", data)
        assert response.status_code == 201
        assert response.json() == data
