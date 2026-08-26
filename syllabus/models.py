from django.db import models

from users.models import User


class Lesson(models.Model):
    title = models.CharField(verbose_name="Название урока")
    description = models.CharField(blank=True, default="Опиcание скоро появится", verbose_name="Описание урока")
    preview = models.ImageField(upload_to="lesson/", verbose_name="Фотография", null=True, blank=True)
    video_link = models.CharField(verbose_name="Сылка на видео")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"
        ordering = ["id", "title"]


class Course(models.Model):
    title = models.CharField(verbose_name="Название курса")
    preview = models.ImageField(upload_to="couse/", verbose_name="Фотография", null=True, blank=True)
    description = models.CharField(blank=True, default="Без опиcания", verbose_name="Описание курса")
    lessons = models.ManyToManyField(Lesson, verbose_name="Уроки курса", blank=True)
    students = models.ManyToManyField(User, verbose_name="Ученики", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"
        ordering = ["id", "title"]
