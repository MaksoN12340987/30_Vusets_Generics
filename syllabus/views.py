import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from rest_framework import generics

from users.models import User

from .forms import CreateCourse, CreateLesson
from .models import Course, Lesson
from .services import SendingMessagesEmail

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


# Main
class MainView(ListView):
    model = Course
    template_name = "syllabus/main.html"
    context_object_name = "lessons"

    def get_queryset(self):
        queryset = Lesson.objects.all()
        # queryset["count_course"] = len(queryset)
        logger_views.info(f"{queryset}")
        # queryset["lessons"] = Lesson.objects.all()
        # queryset = cache.get("main")
        # if not queryset:
        #     queryset = super().get_queryset()
        #     queryset["lessons"] = Lesson.objects.all()
        #     cache.set("main", queryset, 60 * 15)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_course"] = len(Course.objects.all())
        context["count_lesson"] = len(Lesson.objects.all())

        context["users"] = User.objects.all()
        context["count_user"] = len(User.objects.all())

        return context

class CrateObjectLesson(CreateView):
    model = Lesson
    form_class = CreateLesson
    template_name = "syllabus/create.html"
    context_object_name = "Lesson"
    success_url = reverse_lazy("syllabus:main")

class CrateObjectCourse(CreateView):
    model = Course
    form_class = CreateCourse
    template_name = "syllabus/create.html"
    context_object_name = "Course"
    success_url = reverse_lazy("syllabus:main")
