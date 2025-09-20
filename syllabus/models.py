from django.db import models

from users.models import User


class Lesson(models.Model):
    title = models.CharField(verbose_name="Название урока")
    description = models.CharField(
        blank=True, default="Добавьте опиcание", verbose_name="Описание урока"
    )
    preview = models.ImageField(
        upload_to="lesson/", verbose_name="Фотография", null=True, blank=True
    )
    video_link = models.CharField(verbose_name="Сылка на видео")


class Course(models.Model):
    title = models.CharField(verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="couse/", verbose_name="Фотография", null=True, blank=True
    )
    description = models.CharField(
        blank=True, default="Без опиcания", verbose_name="Описание курса"
    )
    lessons = models.ManyToManyField(
        Lesson, verbose_name="Получатели рассылки", null=True, blank=True
    )
