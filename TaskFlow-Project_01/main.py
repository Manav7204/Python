print("Welcome to TaskFlow")

def show_menu():
    print("="*5, "TaskFlow", "="*5)
    print("1. Add Task\n2.View Tasks\n3.Delete\n4.Exit")

def get_menu_choice():
    try:
        choice = int(input("Enter the number of operation: "))
    except ValueError:
        print("\nInvalid input. Enter an integer.\n")
        return None
    
    return choice

def add_task(task_list):
    task_title = input("Enter the Title of the task.\n>").strip()
    if task_title:
        task_list.append(task_title)
        print("\nTask added successfully.\n")
    else:
        print("\nTask cannot be empty!\n")

def view_task(task_list):
    if task_list:
        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i]}\n")
    else:
        print("\nNo Tasks Available.")

def delete_task(task_list, task_id):
    if task_list:            
        task_list.pop(task_id-1)
        print("\nTask Deleted successfully.")
    else:
        print("\nNothing to Delete.")
        
#-----------------------------------------------------------------------#

task_list = [] 

while True:

    show_menu()

    choice = get_menu_choice()

    if choice == 1:
        add_task(task_list)

    elif choice == 2:
        view_task(task_list)

    elif choice == 3:
        try:
            task_id = int(input("Enter the task id to be deleted: "))
        except ValueError:
            print("\nEnter a valid Integer.\n")
            continue

        if 1 <= task_id <= len(task_list):
            delete_task(task_list, task_id)
        else:
            print("\nInvalid task id.\n")

    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("\nEnter Valid Input!\n")