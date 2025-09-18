from django.db import models

from lms.models import Course, Lesson
from users.models import User


class Payment(models.Model):
    """Класс модели платежи."""

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="payment",
        verbose_name="Пользовватель",
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="payment",
        verbose_name="Оплаченный курс",
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="payment",
        verbose_name="Оплаченный урок",
    )
    payment_sum = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        max_length=450,
        verbose_name="Способ оплаты",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Платёж на сумму {self.payment_sum}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
