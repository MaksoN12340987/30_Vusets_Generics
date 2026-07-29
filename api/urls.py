from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import ApiConfig
from .views import (
    ListAPI,
    ListAPICourses,
    ListAPILessons
)

app_name = ApiConfig.name

urlpatterns = [
    path("", ListAPILessons.as_view(), name="list_courses")
]
