from rest_framework.serializers import ValidationError


def video_link_validator(value):
    if "youtube.com" not in value.lower():
        raise ValidationError("Прикрепите ссылку на видео")
