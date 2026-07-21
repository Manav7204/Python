from src.models.status import Status
import logging

logger = logging.getLogger(__name__)


class Task:
    def __init__(self, id: int, title: str, status: Status):
        self._id: int = id
        self.title: str = (
            title  # self.title in place of self._title to all setter work for validation
        )
        self.status = status

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value.strip():
            logger.warning("Task title cannot be empty.")
            raise ValueError("Task title cannot be empty.")
        self._title = value

    def toggle_status(self):
        self.status.toggle()

    def __str__(self) -> str:
        return f"{self.id}. {self.title} [{self.status}]"
