from django.shortcuts import render
from .serializers import TaskSerializers
from  rest_framework import generics
from task.models import Task
# Create your views here.


class TaskDetail( generics.ListAPIView,generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
   

class Task(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    lookup_field= 'pk'


