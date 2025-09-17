from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from lms.models import Course
from subs.models import Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email="test1@mail.com", password="first")
        self.user2 = User.objects.create(email="test2@mail.com", password="second")
        self.course1 = Course.objects.create(
            name="Test course1", description="test1", owner=self.user1
        )
        self.course2 = Course.objects.create(
            name="Test course2", description="test2", owner=self.user2
        )
        self.client.force_authenticate(user=self.user1)
        self.url = "/subs/"

    def test_subscription(self):
        """Тестирование функционала подписки на курс."""

        data = {"course": self.course2.pk}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка добавлена")
        self.assertTrue(Subscription.objects.exists())

    def test_subscription_own(self):
        """Тестирование функционала подписки на свой курс."""

        response = self.client.post(self.url, data={"course": self.course1.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["message"], "Вы не можете подписаться на свой курс"
        )
        self.assertFalse(Subscription.objects.exists())

    def test_subscription_delete(self):
        """Тестирование функционала удаления подписки на курс."""

        Subscription.objects.create(user=self.user1, course=self.course2)
        response = self.client.post(self.url, data={"course": self.course2.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка удалена")
        self.assertFalse(Subscription.objects.exists())
