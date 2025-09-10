from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    """Сериализатор для класса Платежи (Payment)."""

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "phone_number", "city", "avatar")


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "phone_number",
            "city",
            "avatar",
            "password",
        )
