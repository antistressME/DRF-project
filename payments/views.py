from rest_framework import filters
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from payments.models import Payment
from payments.serializer import PaymentSerializer
from payments.services import create_stripe_price, create_stripe_sessions
from users.permissions import IsModer


class PaymentCreateAPIView(CreateAPIView):
    """Класс представления модели Пдлатежей (Payment)."""

    serializer_class = PaymentSerializer
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ("payment_date",)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        price = create_stripe_price(payment.payment_sum)
        payment_link = create_stripe_sessions(price)
        payment.payment_method = payment_link
        payment.save()
