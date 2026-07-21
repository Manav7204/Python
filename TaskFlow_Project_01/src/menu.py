def show_menu():
    print("\n" + "=" * 35)
    print("           TASKFLOW")
    print("=" * 35)
    print(" 1. Add Task")
    print(" 2. View Tasks")
    print(" 3. Search Tasks")
    print(" 4. Update Task")
    print(" 5. Delete Task")
    print(" 6. Exit")
    print("=" * 35)


def get_menu_choice():
        return int(input("Select an option: "))

def edit_menu():
    print("\n" + "-" * 35)
    print("         EDIT TASK")
    print("-" * 35)
    print(" 1. Edit Title")
    print(" 2. Toggle Status")
    print(" 3. Cancel")
    print("-" * 35)
