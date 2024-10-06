from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from .repositories import TaskRepository
from .models import Task
from django.utils import timezone


class TaskSqliteRepository(TaskRepository):
    def get_tasks(self, *args, **kwargs) -> QuerySet:
        is_today = kwargs['is_today']
        tags = kwargs['tags']
        tasks = Task.objects.all()

        if is_today not in ['0', '1']:
            raise ValidationError('u must use is_today=1 or is_today=0')


        if is_today:
            today = timezone.now().date()
            tasks = tasks.filter(deadline__date=today)
        if tags:
            tasks = tasks.filter(tags__name__in=[*(tags.split(','))]).distinct()
        return tasks
