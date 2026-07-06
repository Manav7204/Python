import src.menu, src.task_service

task_list = [] 

while True:

    src.menu.show_menu()

    choice = src.menu.get_menu_choice()

    if choice == 1:
        src.task_service.add_task(task_list)

    elif choice == 2:
        src.task_service.view_task(task_list)

    elif choice == 3:
        try:
            task_id = int(input("Enter the task id to be deleted: "))
        except ValueError:
            print("\nEnter a valid Integer.\n")
            continue

        if 1 <= task_id <= len(task_list):
            src.task_service.delete_task(task_list, task_id)
        else:
            print("\nInvalid task id.\n")

    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("\nEnter Valid Input!\n")