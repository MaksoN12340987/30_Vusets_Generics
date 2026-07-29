import logging

from users.models import User

from rest_framework import generics

from syllabus.models import Course, Lesson

from .serializers import CourseSerializer, LessonSerializer

logger_views = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s",
    datefmt="%H:%M:%S %d-%m-%Y",
)
file_handler.setFormatter(file_formatter)
logger_views.addHandler(file_handler)
logger_views.setLevel(logging.INFO)


class ListAPI(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all(), Lesson.objects.all()

class ListAPICourses(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class ListAPILessons(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Lesson.objects.all()
