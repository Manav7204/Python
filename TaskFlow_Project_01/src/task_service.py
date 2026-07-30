import logging
from src.models.task import Task
from src.models.status import Status
from src.repository.task_repository import TaskRepository

repository = TaskRepository()

logger = logging.getLogger(__name__)


def add_task(task_title):

    task = Task(None, task_title, Status("Pending"))
    task_id = repository.insert_task(task)

    logger.info(f"Task added at ID = {task_id}")


def view_tasks():
    tasks = repository.read_tasks()
    logger.info("Viewed tasks.")
    return tasks


def update_task(task_id, choice, new_title=None):

    task = repository.get_task_by_id(task_id)

    if not task:
        return None

    if choice == 1:

        task.title = new_title
        repository.alter_task(task)

        logger.info(f"Task updated successfully: ID = {task.id}")
        return task

    elif choice == 2:

        task.toggle_status()
        repository.alter_task(task)

        logger.info(f"Status updated successfully: ID = {task.id}")
        return task

    elif choice == 3:
        return None

    else:
        return False


def search_task(keyword):
    logger.info(f"Search performed: {keyword}")
    return repository.retrieve_tasks(keyword)


def delete_task(task_id):
    task = repository.get_task_by_id(task_id)

    if not task:
        return None
    
    repository.delete_task_record(task)
    logger.info(f"Task deleted at ID = {task.id}")
    
    return True