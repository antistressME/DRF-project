from django.core.management import call_command
from django.core.management.base import BaseCommand

from lms.models import Course, Lesson
from payments.models import Payment
from users.models import User


class Command(BaseCommand):
    """Класс создание кастомной кансольной команды для добавления тестовых платежей."""

    help = "Add test payments to the database"

    def handle(self, *args, **kwargs):
        user1, _ = User.objects.get_or_create(email="test@mail.ru")
        user2, _ = User.objects.get_or_create(email="test2@mail.com")
        course1, _ = Course.objects.get_or_create(name="Test course 1")
        course2, _ = Course.objects.get_or_create(name="Test course 2")
        lesson1, _ = Lesson.objects.get_or_create(name="Test lesson 1")
        lesson2, _ = Lesson.objects.get_or_create(name="Test lesson 2")

        payments = [
            {
                "user": user1,
                "payment_date": "2025-01-21 10:30:00",
                "paid_course": course1,
                "paid_lesson": lesson1,
                "payment_sum": "1000",
                "payment_method": "Наличные",
            },
            {
                "user": user1,
                "payment_date": "2025-02-22 20:40:00",
                "paid_course": course2,
                "paid_lesson": lesson2,
                "payment_sum": "2000",
                "payment_method": "Перевод на счёт",
            },
            {
                "user": user2,
                "payment_date": "2024-03-23 13:50:00",
                "paid_course": course2,
                "paid_lesson": lesson2,
                "payment_sum": "3000",
                "payment_method": "Наличные",
            },
        ]

        for payment_data in payments:
            payment, created = Payment.objects.get_or_create(**payment_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added payment: {payment}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Error.payment: {payment}"))
