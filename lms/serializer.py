from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор для класса Курс (Course)."""

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    """Сериализатор для класса Урок (Lesson)."""

    class Meta:
        model = Lesson
        fields = "__all__"
