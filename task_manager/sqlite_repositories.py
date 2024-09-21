from django.db.models import QuerySet
from .repositories import TaskRepository
from .models import Task


class TaskSqliteRepository(TaskRepository):
    def get_all_tasks(self) -> list[QuerySet]:
        return Task.objects.all()
