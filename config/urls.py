from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("materials/", include("lms.urls", namespace="lms")),
    path("payments/", include("users.urls", namespace="payments")),
]
