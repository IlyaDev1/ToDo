from abc import abstractmethod, ABC
from django.db.models import QuerySet


class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> QuerySet:
        ...
