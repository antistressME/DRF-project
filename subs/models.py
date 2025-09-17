from django.db import models

from lms.models import Course, Lesson
from users.models import User


class Subscription(models.Model):
    """Класс модели подписки на обновления курса."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscription",
        verbose_name="Пльзователь",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subscription",
        verbose_name="Курс",
    )

    def __str__(self):
        return f"Подписка {self.user} на курс {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
