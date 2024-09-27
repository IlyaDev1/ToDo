from typing import Type

from django.db.models import QuerySet
from .repositories import TaskRepository
from .serializers import TaskSerializer
from .sqlite_repositories import TaskSqliteRepository
from .models import Task


class TaskService:
    def __init__(self, is_today: bool):
        self.is_today = is_today
        self.task_repository: TaskRepository = TaskSqliteRepository()

    def get_tasks(self) -> QuerySet:
        if self.is_today:
            return self.task_repository.get_today_tasks()
        else:
            return self.task_repository.get_all_tasks()

    def get_task_serializer(self) -> Type[TaskSerializer]:
        return TaskSerializer
