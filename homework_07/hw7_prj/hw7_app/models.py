from django.db import models

# Create your models here.
class Task(models.Model):
    id_task = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, editable=False)
    state_id = models.ForeignKey('State', on_delete=models.PROTECT)
    department_id = models.ForeignKey('Department', on_delete=models.PROTECT)

class State(models.Model):
    id_state = models.IntegerField(primary_key=True)
    state = models.CharField(null=False, max_length=25)

class Department(models.Model):
    id_department = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=90, null=False)
    short_name = models.CharField(max_length=15, null=True, blank=True)