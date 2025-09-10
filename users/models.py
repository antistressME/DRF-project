from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    """Класс пользователя."""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите почту"
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=200,
        verbose_name="Город",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="users/avatars",
        verbose_name="Аватар пользователя (изображение)",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользовватель"
        verbose_name_plural = "Пользовватели"

    def __str__(self):
        return self.email


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
