import pytest
from src.exceptions import EmptyTaskTitleError
from src.models.task import Task
from src.models.status import Status

def test_create_task():
    status = Status("Pending")
    task = Task(None, "Learn Pytest", status)
    
    assert task.title == "Learn Pytest"
    assert task.status.name == "Pending"
    
def test_empty_title():
    
    with pytest.raises(EmptyTaskTitleError):
        Task(None, "", Status("Pending"))
    
def test_whitespace_title():
    with pytest.raises(EmptyTaskTitleError):
        Task(None, "    ", Status("Pending"))
        
def test_toggle_status():
    task = Task(None, "Learn Pytest", Status("Pending"))
    
    task.toggle_status()
    assert task.status.name == "Completed"
    
    task.toggle_status()
    assert task.status.name == "Pending"
    
def test_task_string():
    task = Task(1, "Learn Pytest", Status("Pending"))
    assert str(task) == "1. Learn Pytest [Pending]"