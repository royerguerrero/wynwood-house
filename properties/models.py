"""Properties Models"""

# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Utils
import uuid


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cities/photos')

    def __str__(self) -> str:
        return f'{self.name} ({self.country})'

    class Meta:
        verbose_name_plural = 'cities'


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=125)
    people_capacity = models.PositiveIntegerField(default=1)
    bed_capacity = models.PositiveIntegerField(default=1)
    price_by_night = models.FloatField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def get_photos(self):
        return PropertyPhoto.objects.filter(property=self)

    def __str__(self) -> str:
        return f'{self.name} ({self.address})'

    class Meta:
        verbose_name_plural = 'properties'


class PropertyPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='properties/photos')
