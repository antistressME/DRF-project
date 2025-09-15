from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from lms.models import Course, Lesson
from lms.validators import video_link_validator


class LessonSerializer(ModelSerializer):
    """Сериализатор для класса Урок (Lesson)."""
    video_link = CharField(validators=[video_link_validator])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    """Сериализатор для класса Курс (Course)."""

    lessons_in_course = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lessons_in_course(self, obj):
        # Возвращает количество уроков в курсе.
        lessons_count = Lesson.objects.filter(course=obj).count()
        return lessons_count

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "image",
            "description",
            "lessons_in_course",
            "lesson",
            "owner",
        )
