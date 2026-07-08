import src.menu, src.task_service
from src.storage import store_data, read_data

task_list = read_data()

while True:

    src.menu.show_menu()

    choice = src.menu.get_menu_choice()

    if choice == 1:
        src.task_service.add_task(task_list)

    elif choice == 2:
        src.task_service.view_task(task_list)

    elif choice == 3:
        src.task_service.update_task(task_list)
        
    elif choice == 4:
        src.task_service.delete_task(task_list)

    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("\nEnter Valid Input!\n")