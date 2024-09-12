from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    task_object = models.IntegerField(null=False)
    status = models.IntegerField(null=False, default=100)
    description = models.CharField(max_length=120, null=True, blank=True)
    date_created = models.DateField(auto_now_add=timezone.now())
    time_created = models.TimeField(auto_now_add=timezone.now())
    date_closing = models.DateField(null=True, blank=True)
    time_closing = models.TimeField(null=True, blank=True)


    def __str__(self):
        return f'{self.pk} --> {self.title}  [{self.date_created}]'