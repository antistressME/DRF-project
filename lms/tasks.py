from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from subs.models import Subscription
from users.models import User


@shared_task
def send_email(course):
    """Отправляет письмо на почту."""
    subject = "Обновление курса"
    message = f"Привет! Курс `{course.name}` обновился."
    subs = Subscription.objects.filter(course=course.pk)
    recipient_list = [sub.user.email for sub in subs]
    from_email = EMAIL_HOST_USER
    send_mail(subject, message, from_email, recipient_list)
    print("Send mail to subscribers")


@shared_task
def check_last_login_data():
    users = User.objects.filter(is_active=True)
    for user in users:
        if datetime.now() - user.last_login <= timedelta(days=30):
            user.is_active = False
