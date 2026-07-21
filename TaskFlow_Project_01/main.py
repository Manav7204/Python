from src.menu import show_menu, get_menu_choice
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
            add_task()
        except ValidationError as e:
            print(e)
            logger.error(f"{type(e).__name__}: {e}")

    elif choice == 2:
        view_tasks()

    elif choice == 3:    
        search_task()
        
    elif choice == 4:
        try:
            update_task()
        except ValidationError as e:
            print(e)
            logger.error(f"{type(e).__name__}: {e}")


    elif choice == 5:
        delete_task()

    elif choice == 6:
        print("Goodbye!")
        logging.debug("Application closed")
        break
    else:
        print("\nEnter Valid Input!\n")
