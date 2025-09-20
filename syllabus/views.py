import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from users.models import User

from rest_framework import generics

from .models import Course, Lesson

from .serializers import CourseSerializer, LessonSerializer

from .forms import Create
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
    context_object_name = "newsletters"

    def get_queryset(self):
        queryset = cache.get("ProductListView_queryset")
        if not queryset:
            queryset = super().get_queryset()
        #     cache.set("authors_queryset", queryset, 60 * 15)
        return queryset


# Message API views
class MessageListAPI(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class AttemptSendCreateAPI(generics.CreateAPIView):
    serializer_class = CourseSerializer


# New class
