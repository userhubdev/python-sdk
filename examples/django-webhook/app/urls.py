from django.contrib import admin
from django.urls import path

from app.webhook import webhook_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("webhook", webhook_view),
]
