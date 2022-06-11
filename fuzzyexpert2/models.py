from django.db import models
from django.utils import timezone
from django.urls import reverse

class Student(models.Model):
    fio = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    group = models.CharField(max_length=10)
    lecture = models.CharField(max_length=5, null=False)
    practic = models.CharField(max_length=5, null=False)
    project = models.CharField(max_length=5, null=False)
    visits = models.CharField(max_length=5, null=False)
    score = models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.fio