import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from rest_framework import generics, viewsets
from rest_framework.response import Response

from syllabus.serializers import CourseSerializer
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_course"] = len(Course.objects.all())
        context["count_lesson"] = len(Lesson.objects.all())

        context["users"] = User.objects.all()
        context["count_user"] = len(User.objects.all())

        return context

# API Course
class CourseViewSet(viewsets.ViewSet):
    # queryset = Course.objects.all()
    # serializer_class = CourseSerializer
    def list(self, request):
        # Метод для вывода списка пользователей с определением выборки из базы и указанием сериализатора
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Метод для вывода информации по пользователю с определением выборки из базы и указанием сериализатора
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, request.data)
        
        logger_views.info(f"{request}")
        
        if serializer.is_valid(raise_exception=True):
            serializer.update(course, request.data)
        
        return Response(serializer.data)
    
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)


# API Lesson
class ListLessonsAPI(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()

# class ObjectLessonsAPI(generics.):
#     serializer_class = CourseSerializer
#     queryset = Lesson.objects.all()
