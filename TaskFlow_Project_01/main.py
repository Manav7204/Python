import src.menu, src.task_service
from src.storage import read_data, search_task
from src.database import insert_task,create_table

task_list = read_data()
create_table()

while True:

    src.menu.show_menu()

    choice = src.menu.get_menu_choice()

    if choice == 1:
        insert_task()

    elif choice == 2:
        src.task_service.view_task(task_list)

    elif choice == 3:
        search_task()

    elif choice == 4:
        src.task_service.update_task(task_list)
        
    elif choice == 5:
        src.task_service.delete_task(task_list)

    elif choice == 6:
        print("Goodbye!")
        break
    else:
        print("\nEnter Valid Input!\n")