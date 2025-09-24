from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import SyllabusConfig
from .views import (
    MainView,
)


app_name = SyllabusConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    # API Lesson
    path("lessons/", MessagesView.as_view(), name="lessons"),
    path("lesson/<int:pk>/", MessageDetail.as_view(), name="lesson"),
    path("create_lesson/", MessageCreate.as_view(), name="create_lesson"),
    path("update_lesson/<int:pk>/", MessageUpdate.as_view(), name="update_lesson"),
    path("del_lesson/<int:pk>/", MessageDetail.as_view(), name="del_lesson"),
    # API Course
    path("courses/", MessagesView.as_view(), name="courses"),
    path("course/<int:pk>/", MessageDetail.as_view(), name="course"),
    path("create_course/", MessageCreate.as_view(), name="create_course"),
    path("update_course/<int:pk>/", MessageUpdate.as_view(), name="update_course"),
    path("del_course/<int:pk>/", MessageDetail.as_view(), name="del_course"),
]
