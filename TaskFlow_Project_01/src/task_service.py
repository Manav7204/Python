import logging
from src.models.task import Task
from src.models.status import Status
from src.menu import edit_menu, get_menu_choice
from src.repository.task_repository import TaskRepository

repository = TaskRepository()

logger = logging.getLogger(__name__)


def add_task():

    task_title = input("Enter the Title of the task.\n>").strip()

    task = Task(None, task_title, Status("Pending"))
    task_id = repository.insert_task(task)
    
    logger.info(f"Task added at ID = {task_id}")


def view_tasks():
    tasks = repository.read_tasks()

    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n" + "=" * 40)
    print("             TASK LIST")
    print("=" * 40)

    for task in tasks:
        print(f"• {task}")

    print("=" * 40 + "\n")

    logger.info("Viewed tasks.")


def update_task():

    try:
        task_id = int(input("Enter the task id to update: "))
    except ValueError:
        print("\nEnter a valid Integer.\n")
        logger.warning("Invalid Task ID entered")
        return

    task = repository.get_task_by_id(task_id)

    if not task:
        print("Task not found.")
        return

    edit_menu()
    choice = get_menu_choice()

    if choice == 1:
        new_title = input("Enter the Title of the task.\n>").strip()
    
        task.title = new_title

        repository.alter_task(task)
        print("Task updated Successfully\n")
        
        logger.info(f"Task updated Successfully: ID = {task.id}")

    elif choice == 2:

        task.toggle_status()
        repository.alter_task(task)
        
        print("Status updated Successfully\n")
        logger.info(f"Status updated Successfully: ID = {task.id}")

    elif choice == 3:
        return

    else:
        print("Invalid Choice entered.")



def search_task():
    keyword = input("Enter the Search word: ").strip()

    if not keyword:
        print("Keyword cannot be empty !")
        return

    found_tasks = repository.retrieve_tasks(keyword)

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
        return

    task = repository.get_task_by_id(task_id)

    if not task:
        print("\nNo task found.\n")
        logger.warning("No task found.")
        return

    repository.delete_task_record(task)
    print("\nTask Deleted successfully.")
    logger.info(f"Task deleted at ID = {task.id}")