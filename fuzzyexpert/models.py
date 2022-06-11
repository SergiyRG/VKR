from django.db import models
from django.utils import timezone
from django.urls import reverse

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    c19_result = models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.name