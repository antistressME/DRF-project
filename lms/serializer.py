from rest_framework.serializers import (CharField, ModelSerializer,
                                        SerializerMethodField)

from lms.models import Course, Lesson
from lms.validators import video_link_validator
from subs.models import Subscription


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
    is_sub = SerializerMethodField()

    def get_lessons_in_course(self, obj: Course):
        # Возвращает количество уроков в курсе.
        lessons_count = Lesson.objects.filter(course=obj).count()
        return lessons_count

    def get_is_sub(self, obj: Course):
        user = self.context["request"].user
        if not user or not user.is_authenticated:
            return False
        return Subscription.objects.filter(user=user, course=obj).exists()

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
            "is_sub",
        )
