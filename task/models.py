from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    descriptions= models.TextField(max_length= 200)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.task