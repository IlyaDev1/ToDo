from typing import Type
from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError
from .repositories import TaskRepository
from .serializers import TaskSerializer
from .sqlite_repositories import TaskSqliteRepository
from .validators import TaskValidator


class TaskService:
    def __init__(self):
        self.task_repository: TaskRepository = TaskSqliteRepository()

    def get_tasks(self, get_request: QueryDict) -> QuerySet:
        is_today = get_request.get('is_today')
        tags = get_request.get('tag')

        if TaskValidator.is_today_valid(is_today) and TaskValidator.is_tags_valid(tags):
            if tags:
                tags = tags.split(',')
            return self.task_repository.get_tasks(is_today, tags)

    def get_task_serializer(self) -> Type[TaskSerializer]:
        return TaskSerializer
