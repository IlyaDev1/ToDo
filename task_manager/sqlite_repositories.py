from django.db.models import QuerySet
from .repositories import TaskRepository
from .models import Task
from django.utils import timezone


class TaskSqliteRepository(TaskRepository):
    def get_all_tasks(self) -> QuerySet:
        return Task.objects.all()

    def get_today_tasks(self) -> QuerySet:
        today = timezone.now().date()
        return Task.objects.filter(deadline__date=today)
