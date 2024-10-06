from typing import Type
from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError
from .repositories import TaskRepository
from .serializers import TaskSerializer
from .sqlite_repositories import TaskSqliteRepository
from .models import Task


class TaskService:
    def __init__(self):
        self.task_repository: TaskRepository = TaskSqliteRepository()

    def get_params(self, get_request: QueryDict) -> [bool | None, str | None]:
        return [get_request.get('is_today'), get_request.get('tags')]

    def validate_get_params(self, params: tuple):
        is_today = params[0]
        tags = params[1]

        if is_today:
            if is_today not in ('0', '1'):
                raise ValidationError('u must use is_today=1 or is_today=0')

        if tags:
            try:
                tags = tags.split(',')
            except Exception as e:
                raise ValidationError('u must use tag=tag1,tag2,...')

    def get_tasks(self, get_request: QueryDict) -> QuerySet:
        params =
        return self.task_repository.get_tasks(is_today=is_today, tags=tags)

    def get_task_serializer(self) -> Type[TaskSerializer]:
        return TaskSerializer
