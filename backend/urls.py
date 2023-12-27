from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.mailing.urls")),
    path("user/", include("apps.user.urls")),
    path("admin/", admin.site.urls),
]
