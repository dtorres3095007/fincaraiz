import os
from uuid import uuid4
from django.db import models
from ..cities.models import City
from ..categories.models import Category

# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class Property(models.Model):
    title = models.TextField()
    image = models.FileField(upload_to=path_and_rename)
    price = models.IntegerField()
    city = models.ForeignKey(City,on_delete=models.PROTECT, related_name='property_city',)
    baths = models.IntegerField()
    beds = models.IntegerField()
    sqft = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.PROTECT, related_name='property_category',)

    def __str__(self):
        return self.title
