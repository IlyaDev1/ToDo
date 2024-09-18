from django.urls import path
from .views import TaskCreateAPIView


urlpatterns = [
    path('api/v1/create-task/', TaskCreateAPIView.as_view(), name='task_create_api_view'),
]
