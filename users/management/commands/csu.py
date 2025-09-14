from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Класс создание кастомной кансольной команды для добавления администратора."""

    def handle(self, *args, **options):
        user = User.objects.create(email="new_admin@admin.com")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("1223qwwerty")
        user.save()
