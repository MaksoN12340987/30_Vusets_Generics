from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import SyllabusConfig
from .views import CrateObjectCourse, CrateObjectLesson, MainView

app_name = SyllabusConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("create/lesson/", CrateObjectLesson.as_view(), name="create_les"),
    path("create/course/", CrateObjectCourse.as_view(), name="create_cor"),
]
