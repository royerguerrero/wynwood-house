"""Wynwood House URL Configuration"""

# Django
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# Views
from .views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('', LandingPageView.as_view(), name='landing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
