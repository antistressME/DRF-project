from django.contrib import admin

from lms.models import Course, Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "name",
        "description",
        "owner",
        "course",
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "name",
        "description",
        "owner",
    )
