from django.db import models
from ..property_types.models import PropertyType

class Transaction(models.Model):
    slug = models.TextField()
    property_types = models.ManyToManyField(PropertyType)

    def __str__(self):
        return self.slug
