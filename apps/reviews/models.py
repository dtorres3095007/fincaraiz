from django.db import models

# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'files/images'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class Review(models.Model):
    feedback = models.TextField()
    rating = models.IntegerField()
    avatar = models.FileField(upload_to=path_and_rename)
    date_add = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    state = models.CharField(choices=[("1", "Active"), ("0", "Inactive")], default="1", max_length=10)

    def __str__(self):
        return self.feedback