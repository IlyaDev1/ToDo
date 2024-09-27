from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from .services import TaskService


class TaskBaseAPIView(generics.GenericAPIView):
    task_service: TaskService = None

    def get_queryset(self):
        if self.request.GET.get('today') == '1':
            self.task_service = TaskService(is_today=True)
        else:
            self.task_service = TaskService(is_today=False)

        return self.task_service.get_tasks()

    def get_serializer_class(self):
        return self.task_service.get_task_serializer()


class TaskListCreateAPIView(TaskBaseAPIView, generics.ListCreateAPIView):
    pass


class TaskDetailAPIView(TaskBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass
