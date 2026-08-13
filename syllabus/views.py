import logging

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework import generics, viewsets
from rest_framework.response import Response

from syllabus.serializers import CourseSerializer
from users.models import User

from .models import Course, Lesson

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
    def list(self, request):
        """Получения списка объектов Cource

        Args:
            NONE

        Returns:
            Response: JSON
        """        
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Получения объектa Cource

        Args:
            request: No data
            pk (int): primary key. Defaults to None.

        Returns:
            Response: JSON
        """
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Обновление объектa Cource

        Args:
            request: No data
            pk (int): primary key. Defaults to None.

        Returns:
            Response: JSON
        """
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, request.data)
        
        logger_views.info(f"{request}")
        
        if serializer.is_valid(raise_exception=True):
            serializer.update(course, request.data)
        
        return Response(serializer.data)

    def create(self, request):
        """Создание объектa Cource

        Args:
            request (json): object fields

        Returns:
            Response (json): data
        """        
        course = Course.objects.create()
        serializer = CourseSerializer(course, request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        """Удаление объектa Cource

        Args:
            request: No data
            pk (int): primary key. Defaults to None.

        Returns:
            Response: delete status
        """        
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        
        if course:
            course.delete()        
        
        return Response(f'You destroy instance {request.data}')


# API Lesson
class ListLessonsAPI(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()

class LessonAPI(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()

class UpdateLessonAPI(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()

class DeleteLessonAPI(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()

class CreateLessonAPI(generics.CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()
