from django.db import models

class Category(models.Model):
    slug = models.TextField()

    def __str__(self):
        return self.slug

