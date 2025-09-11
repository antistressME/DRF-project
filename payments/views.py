from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from payments.models import Payment
from payments.serializer import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    """Класс представления модели Пдлатежей (Payment)."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ("payment_date",)
