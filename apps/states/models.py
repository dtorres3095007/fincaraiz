from django.db import models

class State(models.Model):
    slug = models.TextField()

    def __str__(self):
        return self.slug
