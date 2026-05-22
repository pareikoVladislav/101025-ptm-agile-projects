from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
