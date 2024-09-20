from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskBaseAPIView(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPIView(TaskBaseAPIView, generics.CreateAPIView):
    pass


class TaskListAPIView(TaskBaseAPIView, generics.ListAPIView):
    pass


class TaskUpdateAPIView(TaskBaseAPIView, generics.UpdateAPIView):
    pass


class TaskDeleteAPIView(TaskBaseAPIView, generics.DestroyAPIView):
    pass
