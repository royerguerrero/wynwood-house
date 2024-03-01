"""Wynwood House views."""

# Django
from typing import Any
from django.views.generic import ListView

# Models
from properties.models import Property, City


class LandingPageView(ListView):
    model = Property
    template_name = 'landing.html'
    context_object_name = 'properties'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()[:3]

        return context
