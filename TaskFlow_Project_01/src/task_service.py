from src.database import (
    insert_task,
    read_tasks,
    alter_task,
    delete_task_record,
    retrieve_tasks,
    get_task_by_id,
)
import logging
from src.models.task import Task

logger = logging.getLogger(__name__)


def add_task():

    task_title = input("Enter the Title of the task.\n>").strip()

    if task_title:
        task = Task(None, task_title)
        task_id = insert_task(task)
        logger.info(f"Task added at ID = {task_id}")
    else:
        print("\nTask cannot be empty!\n")
        logger.warning("Empty Task title")
        return None


def view_tasks():
    tasks = read_tasks()
    if tasks:
        print("\n\n")
        print("-" * 10, "Task List", "-" * 10)
        for task in tasks:
            print(task)
        print("\n\n")
        logger.info("Viewed Tasks")
    else:
        print("\nNo Tasks Available.")


def update_task():
    try:
        task_id = int(input("Enter the task id to update: "))
    except ValueError:
        print("\nEnter a valid Integer.\n")
        logger.warning("Invalid Task ID entered")
        return None

    task = get_task_by_id(task_id)
    if task:
        task_title = input("Enter the Title of the task.\n>").strip()

        if task_title:
            alter_task(task_title, task_id)
            print("Task updated Successfully\n")
            logger.info(f"Task updated Successfully: ID = {task_id}")

        else:
            print("\nTask cannot be empty!\n")
            return None

    else:
        print("Task not found.")
        return None


def search_task():
    keyword = input("Enter the Search word: ").strip()

    if not keyword:
        print("Keyword cannot be empty !")
        return

    found_tasks = retrieve_tasks(keyword)

    logger.info(f"Search performed: {keyword}")

    if found_tasks:
        print(f"Found {len(found_tasks)} matches -->")

        for task in found_tasks:
            print(task)
    else:
        print("No match found !")
        return


def delete_task():
    try:
        task_id = int(input("Enter the task id to Delete: "))
    except ValueError:
        print("\nEnter a valid Integer.\n")
        return None

    task = get_task_by_id(task_id)

    if task:
        delete_task_record(task_id)
        print("\nTask Deleted successfully.")
        logger.info(f"Task deleted at ID = {task_id}")
    else:
        print("\nNo task found.\n")
        logger.warning("No task found.")
        return None
