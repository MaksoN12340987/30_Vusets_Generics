from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from users.apps import UsersConfig
from syllabus.apps import SyllabusConfig

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        include(f"{SyllabusConfig.name}.urls", namespace=f"{SyllabusConfig.name}"),
    ),
    path(
        f"{UsersConfig.name}/",
        include(f"{UsersConfig.name}.urls", namespace=f"{UsersConfig.name}"),
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
