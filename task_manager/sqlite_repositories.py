from django.db.models import QuerySet
from .repositories import TaskRepository
from .models import Task
from django.utils import timezone


class TaskSqliteRepository(TaskRepository):
    def get_tasks(self, *args, **kwargs) -> QuerySet:
        is_today = kwargs['is_today']
        tag = kwargs['tag']
        tasks = Task.objects.all()

        if is_today:
            today = timezone.now().date()
            tasks = tasks.filter(deadline__date=today)
        if tag:
            tasks = tasks.filter(tags__name__in=[tag])
        return tasks
