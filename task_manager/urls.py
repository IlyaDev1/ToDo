from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView


urlpatterns = [
    path('task/', TaskListCreateAPIView.as_view(), name='task_list_create_api_view'),
    path('task/<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail_api_view'),
]
