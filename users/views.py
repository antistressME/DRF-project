from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializer import (UserRetrieveSerializer, UserSerializer,
                              UserUpdateSerializer)


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
