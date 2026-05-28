from django.core.validators import MinLengthValidator
from django.db import models
from projects.enums import STATUSES_CHOICES
from projects.enums import PRIORITY_CHOICES
from django.contrib.auth.models import  User


class Task(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    description = models.TextField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUSES_CHOICES)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due_date = models.DateTimeField()

    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')

    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",

    )

    def __str__(self):
        return self.name


