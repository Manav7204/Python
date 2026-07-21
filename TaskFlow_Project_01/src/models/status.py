import logging

logger = logging.getLogger(__name__)


class Status:
    def __init__(self, name: str):
        self.name = name

    def toggle(self):
        if self.name == "Pending":
            self.name = "Completed"
        else:
            self.name = "Pending"

    def __str__(self):
        return self.name
