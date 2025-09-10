from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializer import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    """Класс представления модели Пдлатежей (Payment)."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ("payment_date", "paid_course", "paid_lesson", "payment_method")
