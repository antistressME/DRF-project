from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """Сериализатор для класса Урок (Lesson)."""

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
        fields = ("id", "name", "image", "description", "lessons_in_course", "lesson", "owner")
