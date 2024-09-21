from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from .services import TaskService


class TaskBaseAPIView(generics.GenericAPIView):
    queryset = TaskService.get_all_tasks()
    serializer_class = TaskService.get_task_serializer()


class TaskListCreateAPIView(TaskBaseAPIView, generics.ListCreateAPIView):
    pass


class TaskDetailAPIView(TaskBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass
