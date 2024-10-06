from abc import abstractmethod, ABC
from django.db.models import QuerySet


class TaskRepository(ABC):
    @abstractmethod
    def get_tasks(self) -> QuerySet:
        ...
