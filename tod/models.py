from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Todo(models.Model):
    task=models.CharField(max_length=20)
    des=models.CharField(max_length=100)
    date=models.DateField()