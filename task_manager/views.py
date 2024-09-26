from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from .services import TaskService


class TaskBaseAPIView(generics.GenericAPIView):
    task_service = TaskService()

    def get_queryset(self):
        return self.task_service.get_tasks()

    def get_serializer_class(self):
        return self.task_service.get_task_serializer()


class TaskListCreateAPIView(TaskBaseAPIView, generics.ListCreateAPIView):
    pass


class TaskDetailAPIView(TaskBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass
