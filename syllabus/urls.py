from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import SyllabusConfig
from .views import CourseViewSet, ListLessonsAPI, MainView

app_name = SyllabusConfig.name

router = DefaultRouter()
router.register(r'Course', CourseViewSet, basename='course')

urlpatterns = [
    path("main/", MainView.as_view(), name="main"),
    
    # API Generic
    path("list_lessonss/", ListLessonsAPI.as_view(), name="list_lessonss"),
    
    # API ViewSet
    path("course_viewset/", include(router.urls)),
]
