class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return f"{self.id}. {self.title}"