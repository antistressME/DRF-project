from django.db import models

from lms.models import Course, Lesson
from users.models import User


class Payment(models.Model):
    """Класс модели платежи."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payment",
        verbose_name="Пользовватель",
    )
    payment_date = models.DateTimeField(verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="payment",
        verbose_name="Оплаченный курс",
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="payment",
        verbose_name="Оплаченный урок",
    )
    payment_sum = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=150, verbose_name="Способ оплаты")

    def __str__(self):
        return f"Платёж на сумму {self.payment_sum}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
