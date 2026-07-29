import pytest

from src.repository.task_repository import TaskRepository
from src.models.task import Task
from src.models.status import Status

def test_insert_task():
    
    # Arrange
    repo = TaskRepository()
    
    # Act
    task = Task(None, "Learn Pytest", Status("Pending"))
    task_id = repo.insert_task(task)
    
    # Assert
    assert task_id is not None

def test_read_tasks():
    
    repo = TaskRepository()
    
    tasks = repo.read_tasks()
    
    assert isinstance(tasks, list)
    
    if tasks:
        assert isinstance(tasks[0], Task)

def test_get_task_by_id():
    
    repo = TaskRepository()
    
    task = Task(None, "Get BY ID", Status("Pending"))
    task_id = repo.insert_task(task)
    
    fetched_task = repo.get_task_by_id(task_id)
    
    assert fetched_task is not None
    assert fetched_task.id == task_id
    assert fetched_task.title == "Get BY ID"
    
    if fetched_task:
        assert isinstance(fetched_task, Task)
    
def test_alter_task():
    repository = TaskRepository()

    task = Task(None, "Old Title", Status("Pending"))
    task_id = repository.insert_task(task)

    updated_task = repository.get_task_by_id(task_id)
    updated_task.title = "New Title"

    repository.alter_task(updated_task)

    fetched_task = repository.get_task_by_id(task_id)

    assert fetched_task.title == "New Title"


def test_retrieve_tasks():
    repository = TaskRepository()

    task = Task(None, "Python Testing", Status("Pending"))
    repository.insert_task(task)

    results = repository.retrieve_tasks("Python")

    assert len(results) > 0

    for task in results:
        assert "Python" in task.title


def test_delete_task_record():
    repository = TaskRepository()

    task = Task(None, "Delete Me", Status("Pending"))
    task_id = repository.insert_task(task)

    task = repository.get_task_by_id(task_id)

    repository.delete_task_record(task)

    deleted_task = repository.get_task_by_id(task_id)

    assert deleted_task is None