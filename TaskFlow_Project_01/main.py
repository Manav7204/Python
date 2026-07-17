from src.menu import show_menu, get_menu_choice
from src.task_service import add_task, view_tasks, update_task, delete_task, search_task
from src.database import create_table
from config import setup_logging
import logging

setup_logging()
logging.debug("Application Started.")
create_table()

while True:

    show_menu()

    choice = get_menu_choice()

    if choice == 1:
        add_task()

    elif choice == 2:
        view_tasks() 

    elif choice == 3:
        search_task()

    elif choice == 4:
        update_task()
        
    elif choice == 5:
        delete_task()

    elif choice == 6:
        print("Goodbye!")
        logging.debug("Application closed")
        break
    else:
        print("\nEnter Valid Input!\n")