from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from lms.models import Course, Lesson
from lms.serializer import CourseSerializer, LessonSerializer
from users.permissions import IsModer


class CourseViewSet(ModelViewSet):
    """Класс представления для курса."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            self.permission_classes = [~IsModer]
        elif self.action in ["retrieve", "update"]:
            self.permission_classes = [IsModer]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(CreateAPIView):
    """Класс представления для создания урока."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """Класс представления для вывода списка уроков."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    """Класс представления для вывода урока."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer]


class LessonUpdateAPIView(UpdateAPIView):
    """Класс представления для обновления, изменения данных урока."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModer]


class LessonDestroyAPIView(DestroyAPIView):
    """Класс представления для удаления урока."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModer]
