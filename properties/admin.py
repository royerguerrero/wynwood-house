"""Properties admin"""

# Django
from django.contrib import admin

# Models
from properties.models import Property, PropertyPhoto, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


class PropertyPhotoInline(admin.StackedInline):
    model = PropertyPhoto
    extra = 3


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyPhotoInline,]
