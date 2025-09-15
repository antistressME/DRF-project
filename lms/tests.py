from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from lms.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@mail.com", password="test")
        self.course = Course.objects.create(
            name="Test course", description="test", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_course_create(self):
        """Тест создания курса."""

        url = "/materials/"
        data = {"name": "new course", "description": "test"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)
        self.assertEqual(response.json().get("owner"), self.user.pk)

    def test_course_detail(self):
        """Тест просмотр данных курса."""

        url = f"/materials/{self.course.pk}/"
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test course")
        self.assertEqual(data.get("owner"), self.user.pk)

    def test_course_update(self):
        """Тест обновления курса."""

        url = f"/materials/{self.course.pk}/"
        new_data = {
            "name": "new name",
            "description": "new description",
        }
        response = self.client.patch(url, new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("name"), "new name")
        self.assertEqual(response.json().get("description"), "new description")

    def test_course_delete(self):
        """Тест удаления курса."""

        url = f"/materials/{self.course.pk}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@mail.com", password="test")
        self.course = Course.objects.create(name="Test course", description="test")
        self.lesson = Lesson.objects.create(
            name="Test lesson", description="test", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        """Тест создания урока."""

        url = reverse("lms:lesson_create")
        data = {
            "name": "new lesson",
            "description": "test",
            "course": self.course.pk,
            "video_link": "youtube.com",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(response.json().get("owner"), self.user.pk)

    def test_lesson_detail(self):
        """Тест просмотр данных урока."""

        url = reverse("lms:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test lesson")
        self.assertEqual(data.get("owner"), self.user.pk)

    def test_lesson_update(self):
        """Тест обновления урока."""

        url = reverse("lms:lesson_update", args=(self.lesson.pk,))
        new_data = {
            "name": "new name",
            "description": "new description",
        }
        response = self.client.patch(url, new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("name"), "new name")
        self.assertEqual(response.json().get("description"), "new description")

    def test_lesson_delete(self):
        """Тест удаления урока."""

        url = reverse("lms:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)
