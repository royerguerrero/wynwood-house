"""Wynwood House URL Configuration"""

# Django
from django.contrib import admin
from django.urls import include, path

# Views
from .views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('', LandingPageView.as_view(), name='landing'),
]
