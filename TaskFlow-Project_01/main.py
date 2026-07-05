print("Welcome to TaskFlow")

task_list = []
while True:
    print("="*5, "TaskFlow", "="*5)
    print("1. Add Task\n2.Exit")

    try:
        choice = int(input("Enter the number of operation: "))
    except ValueError:
        print("Invalid input. Enter an integer.")
        continue

    if choice == 1:
        task_title = input("Enter the Title of the task.\n>").strip()
        if task_title:
            task_list.append(task_title)
            print("Task added successfully.")
        else:
            print("Task cannot be empty!")
    elif choice == 2:
        print("Goodbye!")
        break
    else:
        print("Enter Valid Input !")

print(task_list)