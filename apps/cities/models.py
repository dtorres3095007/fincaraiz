from django.db import models
from ..states.models import State

class City(models.Model):
    slug = models.TextField()
    zipp = models.IntegerField()
    state = models.ForeignKey(State,on_delete=models.PROTECT, related_name='state_city',)

    def __str__(self):
        return self.slug
