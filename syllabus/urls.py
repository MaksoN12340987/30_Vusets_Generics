from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import SyllabusConfig
from .views import (
    MainView
)

app_name = SyllabusConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
]


