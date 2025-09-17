from rest_framework.serializers import ModelSerializer

from subs.models import Subscription


class SubscriptionSerializer(ModelSerializer):
    """Сериализатор для класса Подписки (Subscription)."""

    class Meta:
        model = Subscription
        fields = "__all__"
