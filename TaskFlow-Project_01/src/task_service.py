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