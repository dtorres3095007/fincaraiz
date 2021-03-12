import os
from uuid import uuid4
from django.db import models

# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class Review(models.Model):
    feedback = models.TextField()
    rating = models.IntegerField()
    avatar = models.FileField(upload_to=path_and_rename)

    def __str__(self):
        return self.feedback
