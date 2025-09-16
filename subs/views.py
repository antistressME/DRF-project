from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from lms.models import Course
from subs.models import Subscription
from subs.serializer import SubscriptionSerializer
from users.permissions import IsModer


class SubscriptionViewSet(ModelViewSet):
    """Класс представления создания подписки."""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [~IsModer, IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course"]
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_id)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        else:
            if user == course_item.owner:
                message = "Вы не можете подписаться на свой курс"
            else:
                Subscription.objects.create(course=course_item, user=user)
                message = "Подписка добавлена"
        return Response({"message": message})
