from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="static/avatar")

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY = (
        ("low", "low"),
        ("medium", "medium"),
        ("high", "high"),
        ("urgent", "urgent"),
    )

    name = models.CharField(max_length=255)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateField()
    priority = models.CharField(
        max_length=255,
        choices=PRIORITY,
        default="low",
    )
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return self.name
