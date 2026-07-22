import pytest
from src.models.status import Status
from src.task_service import add_task

def test_create_status():
    status = Status("Pending")
    assert status.name == "Pending"

def test_toggle__pending_to_completed():
    status = Status("Pending")

    status.toggle()
    
    assert status.name == "Completed"
    
def test_toggle__completed_to_completed():
    status = Status("Completed")

    status.toggle()
    
    assert status.name == "Pending"
    
def test_status_string():
    status = Status("Pending")
    
    assert str(status) == "Pending"