from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from .repositories import TaskRepository
from .models import Task
from django.utils import timezone


class TaskSqliteRepository(TaskRepository):
    def get_tasks(self, is_today: str | None, tags: str | None) -> QuerySet:
        tasks = Task.objects.all()

        if is_today:
            today = timezone.now().date()
            tasks = tasks.filter(deadline__date=today)
        if tags:
            tasks = tasks.filter(tags__name__in=tags).distinct()
        return tasks
