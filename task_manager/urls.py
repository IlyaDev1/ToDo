from django.urls import path
from .views import TaskCreateAPIView, TaskListAPIView, TaskUpdateAPIView


urlpatterns = [
    path('', TaskListAPIView.as_view(), name='task_list_api_view'),
    path('api/v1/create-task/', TaskCreateAPIView.as_view(), name='task_create_api_view'),
    path('api/v1/update-task/<int:pk>/', TaskUpdateAPIView.as_view(), name='task_update_api_view'),
]
