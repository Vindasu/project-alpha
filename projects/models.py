from django.db import models
from django.conf import settings

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="projects"
    )

    def __str__(self):
        return self.name
