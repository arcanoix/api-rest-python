from django.db import models


# Create your models here.
class Task(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=True)

    def __str__(self):
        return self.title
