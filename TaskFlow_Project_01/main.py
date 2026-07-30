from src.menu import show_menu, get_menu_choice, edit_menu
from src.task_service import add_task, view_tasks, update_task, delete_task, search_task
from src.database import create_table
from src.exceptions import ValidationError, DatabaseError
import logging
from config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

logger.debug("Application Started.")

try:
    create_table()
except DatabaseError as e:
    print(e)
    logger.exception(e)
    exit(1)

while True:

    show_menu()

    try:
        choice = get_menu_choice()
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        try:
            task_title = input("Enter the Title of the task.\n>").strip()
            add_task(task_title)
            print("Task Added Successfully.")
        except ValidationError as e:
            print(e)
            logger.error(f"{type(e).__name__}: {e}")

    elif choice == 2:
        tasks = view_tasks()

        if not tasks:
            print("\nNo tasks available.\n")
        else:
            print("\n" + "=" * 40)
            print("             TASK LIST")
            print("=" * 40)

        for task in tasks:
            print(f"• {task}")

        print("=" * 40 + "\n")

    elif choice == 3:
        keyword = input("Enter the Search word: ").strip()

        if not keyword:
            print("Empty Search Parameter")
        else:
            tasks = search_task(keyword)
            if not tasks:
                print("No matching tasks found.\n")
            else:
                print("\n" + "=" * 40)
                print("          SEARCH RESULTS")
                print("=" * 40)

                for task in tasks:
                    print(f"• {task}")

                print("=" * 40 + "\n")

    elif choice == 4:
        try:
            task_id = int(input("Enter the task ID to update: "))
        except ValueError:
            print("\nEnter a valid integer.\n")
        else:
            edit_menu()
            choice = get_menu_choice()

            if choice == 1:
                new_title = input("Enter the new title:\n> ").strip()
                result = update_task(task_id, choice, new_title)

            else:
                result = update_task(task_id, choice)

        if result is None:
            print("Task not found.")

        elif result is False:
            print("Invalid choice entered.")

        else:
            print("Task updated successfully.\n")

    elif choice == 5:
        try:
            task_id = int(input("Enter the task ID to delete: "))
        except ValueError:
            print("\nEnter a valid integer.\n")

        if delete_task(task_id):
            print("Task Deleted Successfully.")
        else:
            print("Task not found.")

    elif choice == 6:
        print("Goodbye!")
        logging.debug("Application closed")
        break
    else:
        print("\nEnter Valid Input!\n")
