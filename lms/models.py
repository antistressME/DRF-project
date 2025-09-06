from django.db import models


class Course(models.Model):
    """Класс модели курса."""

    name = models.CharField(max_length=150, verbose_name="Название курса")
    image = models.ImageField(upload_to="lms/course/images/", verbose_name="Превью")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    """Класс модели урока."""

    name = models.CharField(max_length=150, verbose_name="Название урока")
    image = models.ImageField(upload_to="lms/lesson/images/", verbose_name="Превью")
    description = models.TextField(verbose_name="Описание урока")
    video_link = models.URLField(max_length=150, verbose_name="Ссылка на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
