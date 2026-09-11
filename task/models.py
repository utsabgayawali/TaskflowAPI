from django.db import models



class Task(models.Model):
    task = models.CharField(max_length=50)
    descriptions= models.TextField(max_length= 200)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.task