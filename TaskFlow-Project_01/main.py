print("Welcome to TaskFlow")

def show_menu():
    print("="*5, "TaskFlow", "="*5)
    print("1. Add Task\n2.Exit")

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

#-----------------------------------------------------------------------#

task_list = []  

while True:

    show_menu()

    choice = get_menu_choice()

    if choice == 1:
        add_task(task_list)
    elif choice == 2:
        print("Goodbye!")
        break
    else:
        print("\nEnter Valid Input!\n")

# while True:
#     print("="*5, "TaskFlow", "="*5)
#     print("1. Add Task\n2.Exit")

#     try:
#         choice = int(input("Enter the number of operation: "))
#     except ValueError:
#         print("Invalid input. Enter an integer.")
#         continue

#     if choice == 1:
#         task_title = input("Enter the Title of the task.\n>").strip()
#         if task_title:
#             task_list.append(task_title)
#             print("Task added successfully.")
#         else:
#             print("Task cannot be empty!")
#     elif choice == 2:
#         print("Goodbye!")
#         break
#     else:
#         print("Enter Valid Input !")
