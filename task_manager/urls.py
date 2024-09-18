from django.urls import path
from .views import TaskCreateAPIView, TaskListAPIView


urlpatterns = [
    path('', TaskListAPIView.as_view(), name='task_list_api_view'),
    path('api/v1/create-task/', TaskCreateAPIView.as_view(), name='task_create_api_view'),
]
