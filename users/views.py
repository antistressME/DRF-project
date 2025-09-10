from rest_framework import filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializer import (PaymentSerializer, UserRetrieveSerializer,
                              UserSerializer, UserUpdateSerializer)


class PaymentViewSet(ModelViewSet):
    """Класс представления модели Пдлатежей (Payment)."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ("payment_date",)


class UserCreateAPIView(CreateAPIView):
    """Класс представления для создания пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    """Класс представления для просмотра данных пользователя."""

    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


class UserUpdateAPIView(UpdateAPIView):
    """Класс представления для обновления данных пользователя."""

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDestroyAPIView(DestroyAPIView):
    """Класс представления для удаления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
