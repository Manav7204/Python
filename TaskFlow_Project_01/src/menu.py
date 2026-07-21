def show_menu():
    print("="*5, "TaskFlow", "="*5)
    print("1. Add Task\n2. View Tasks\n3. Search\n4. Update\n5. Delete\n6. Exit")
    print("="*20)

def get_menu_choice():
    try:
        choice = int(input("Enter the number of operation to perform: "))
    except ValueError:
        print("\nInvalid input. Enter an integer.\n")
        return None
    
    return choice

def edit_menu():
    print("\n","="*5, "TaskFlow", "="*5)
    print("1. Edit task Title\n2. Edit Status\n3. Cancel")
    print("="*20, "\n")
