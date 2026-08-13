from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import SyllabusConfig
from .views import CourseViewSet, CreateLessonAPI, DeleteLessonAPI, LessonAPI, ListLessonsAPI, MainView, UpdateLessonAPI

app_name = SyllabusConfig.name

router = DefaultRouter()
router.register(r'Course', CourseViewSet, basename='course')

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    
    # API Generic
    path("list_lessonss/", ListLessonsAPI.as_view(), name="list_lessonss"),
    path("lesson/<int:pk>/", LessonAPI.as_view(), name="lesson"),
    path("lesson/<int:pk>/update/", UpdateLessonAPI.as_view(), name="lesson_update"),
    path("lesson/<int:pk>/delete/", DeleteLessonAPI.as_view(), name="lesson_delete"),
    path("lesson/", CreateLessonAPI.as_view(), name="lesson_create"),
    
    # API ViewSet
    path("course_viewset/", include(router.urls)),
]
