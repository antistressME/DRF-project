from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from subs.models import Subscription


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
