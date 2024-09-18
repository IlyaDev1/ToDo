from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializerForCreate, TaskSerializer, TaskSerializerForUpdate


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerForCreate


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerForUpdate


class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
