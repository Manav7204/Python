from unittest.mock import patch

from src.task_service import (
    add_task,
    view_tasks,
    update_task,
    search_task,
    delete_task,
)

from src.models.task import Task
from src.models.status import Status


@patch("src.task_service.repository")
def test_add_task(mock_repository):

    # Arrange
    mock_repository.insert_task.return_value = 1

    # Act
    add_task("Learn Pytest")

    # Assert
    mock_repository.insert_task.assert_called_once()

    task = mock_repository.insert_task.call_args.args[0]

    assert isinstance(task, Task)
    assert task.title == "Learn Pytest"
    assert task.status.name == "Pending"


@patch("src.task_service.repository")
def test_view_tasks(mock_repository):

    # Arrange
    task = Task(1, "Learn Pytest", Status("Pending"))
    mock_repository.read_tasks.return_value = [task]

    # Act
    tasks = view_tasks()

    # Assert
    mock_repository.read_tasks.assert_called_once()
    assert len(tasks) == 1
    assert tasks[0].title == "Learn Pytest"


@patch("src.task_service.repository")
def test_search_task(mock_repository):

    # Arrange
    task = Task(1, "Python Testing", Status("Pending"))
    mock_repository.retrieve_tasks.return_value = [task]

    # Act
    tasks = search_task("Python")

    # Assert
    mock_repository.retrieve_tasks.assert_called_once_with("Python")
    assert len(tasks) == 1
    assert tasks[0].title == "Python Testing"


@patch("src.task_service.repository")
def test_update_task_title(mock_repository):

    # Arrange
    task = Task(1, "Old Title", Status("Pending"))

    mock_repository.get_task_by_id.return_value = task

    # Act
    update_task(1, 1, "New Title")

    # Assert
    mock_repository.get_task_by_id.assert_called_once_with(1)
    mock_repository.alter_task.assert_called_once()

    updated_task = mock_repository.alter_task.call_args.args[0]

    assert updated_task.title == "New Title"


@patch("src.task_service.repository")
def test_update_task_status(mock_repository):

    # Arrange
    task = Task(1, "Task", Status("Pending"))

    mock_repository.get_task_by_id.return_value = task

    # Act
    update_task(1, 2)

    # Assert
    mock_repository.get_task_by_id.assert_called_once_with(1)
    mock_repository.alter_task.assert_called_once()

    updated_task = mock_repository.alter_task.call_args.args[0]

    assert updated_task.status.name == "Completed"


@patch("src.task_service.repository")
def test_delete_task(mock_repository):

    # Arrange
    task = Task(1, "Delete Me", Status("Pending"))
    mock_repository.get_task_by_id.return_value = task

    # Act
    delete_task(1)

    # Assert
    mock_repository.get_task_by_id.assert_called_once_with(1)
    mock_repository.delete_task_record.assert_called_once_with(task)