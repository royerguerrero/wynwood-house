"""Properties Tag Extras"""

# Django
from django import template

register = template.Library()


@register.filter(name='get_photos')
def get_photos(property):
    return property.get_photos()
