from django.urls import path

from django.conf import settings

from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("index.html", views.index, name="index"),
    path("about.html", views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
