from typing import Type
from django.db.models import QuerySet
from django.http import QueryDict
from .repositories import TaskRepository
from .serializers import TaskSerializer
from .sqlite_repositories import TaskSqliteRepository
from .models import Task


class TaskService:
    def __init__(self):
        self.task_repository: TaskRepository = TaskSqliteRepository()

    def get_tasks(self, get_request: QueryDict) -> QuerySet:
        is_today = get_request.get('today')
        tag = get_request.get('tag')
        return self.task_repository.get_tasks(is_today=is_today, tag=tag)

    def get_task_serializer(self) -> Type[TaskSerializer]:
        return TaskSerializer
