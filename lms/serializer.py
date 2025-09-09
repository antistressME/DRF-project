from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор для класса Курс (Course)."""

    lessons_in_course = SerializerMethodField()

    def get_lessons_in_course(self, obj):
        # Возвращает количеств уроков в курсе.
        lessons_count = Lesson.objects.filter(course=obj.pk).count()
        return lessons_count

    class Meta:
        model = Course
        fields = ("name", "image", "description", "lessons_in_course")


class LessonSerializer(ModelSerializer):
    """Сериализатор для класса Урок (Lesson)."""

    class Meta:
        model = Lesson
        fields = "__all__"
